PACKAGE_NAME        = workflows.client
PACKAGE_DESCRIPTION = Python client for Argo Workflows

CURRENT_DIR ?= $(shell pwd)
OUTPUT_DIR  ?= ./

define get_branch
$(shell git branch | sed -n '/\* /s///p')
endef

define get_tag
$(shell \
	if [ -z "`git status --porcelain`" ]; then \
		git describe \
			--exact-match \
			--tags HEAD 2>/dev/null || (>&2 echo "Tag has not been created.") \
	fi \
)
endef

define get_tree_state
$(shell \
	if [ -z "`git status --porcelain`" ]; then \
		echo "clean" \
	else \
		echo "dirty" \
	fi
)
endef

GIT_COMMIT     = $(shell git rev-parse HEAD)

GIT_BRANCH     = $(call get_branch)
GIT_TAG        = $(call get_tag)
GIT_TREE_STATE = $(call get_tree_state)

ifeq (${GIT_TAG},)
GIT_TAG = $(shell git rev-parse --abbrev-ref HEAD)
endif

CLIENT_VERSION    ?= $(shell echo $${GIT_BRANCH/release-/})

ARGO_VERSION      ?= 2.3.0
ARGO_API_GROUP    ?= argoproj.io
ARGO_API_VERSION  ?= v1alpha1
ARGO_OPENAPI_SPEC  = openapi/specs/argo-${ARGO_VERSION}.json

KUBERNETES_BRANCH      ?= release-1.12
KUBERNETES_OPENAPI_SPEC = openapi/specs/kubernetes-${KUBERNETES_BRANCH}.json

OPENAPI_SPEC   = openapi/swagger.json
OPENAPI_CONFIG = openapi/custom/config.json

PYPI_REPOSITORY ?= https://upload.pypi.org/legacy/

.PHONY: all
all: clean validate spec preprocess client


.PHONY: clean
clean:
	-rm -r ${OUTPUT_DIR}/argo/workflows/client
	-rm -r ${OUTPUT_DIR}/docs/

	pushd openapi/ ; git clean -d --force ; popd

.PHONY: release
release: SHELL:=/bin/bash
release: all changelog
	- rm -rf build/ dist/

	sed -i "s/__version__ = \(.*\)/__version__ = \"${CLIENT_VERSION}\"/g" argo/workflows/__about__.py

	python setup.py sdist bdist_wheel
	twine check dist/* || (echo "Twine check did not pass. Aborting."; exit 1)

	git commit -a -m "Release ${CLIENT_VERSION}" --signoff
	git tag -a "v${CLIENT_VERSION}" -m "Release ${CLIENT_VERSION}"

	git push origin ${GIT_BRANCH}
	git push origin ${GIT_BRANCH} --tags

	# twine upload --repository-url "${PYPI_REPOSITORY}" dist/* -u "${PYPI_USERNAME}" -p "${PYPI_PASSWORD}"

validate:
	@echo "Validating version '${CLIENT_VERSION}' on branch '{GIT_BRANCH}'"

	if [ "$(shell python -c \
		"from semantic_version import validate; print( validate('${CLIENT_VERSION}') )" \
	)" != "True" ]; then \
		echo "Invalid version. Aborting."; \
		exit 1; \
	fi

spec: 
	# Make sure the folders exist
	mkdir -p openapi/specs/

	@echo "Collecting API spec for Argo ${ARGO_VERSION}"
	curl -sSL https://raw.githubusercontent.com/kubernetes/kubernetes/${KUBERNETES_BRANCH}/api/openapi-spec/swagger.json \
		-o ${KUBERNETES_OPENAPI_SPEC}
	
	@echo "Collecting API spec for Kubernetes ${KUBERNETES_BRANCH}"
	curl -sSL https://raw.githubusercontent.com/argoproj/argo/v${ARGO_VERSION}/api/openapi-spec/swagger.json \
		-o ${ARGO_OPENAPI_SPEC}

	@echo "Extracting definitions"
	jq -r '{ definitions: .definitions }' ${ARGO_OPENAPI_SPEC} \
		> openapi/definitions/argo.json

	@echo "Merging API definitions"
	jq -sS '.[0] * .[1] * .[2] * .[3] * .[4]' \
		openapi/definitions/argo.json \
		openapi/definitions/NodeStatus.json \
		openapi/definitions/TemplateRef.json \
		openapi/definitions/V1Time.json \
		openapi/definitions/WorkflowStatus.json \
		> openapi/definitions.json

	@echo "Creating OpenAPI info"
	echo '{"info": {"title": "Argo", "description": "${PACKAGE_DESCRIPTION}", "version": "${ARGO_VERSION}"}}' | jq -r '.' \
		> openapi/info.json

	@echo "Process OpenAPI paths"
	jinja2 openapi/custom/paths.json --format=json --strict \
		-Dargo_api_group=${ARGO_API_GROUP} \
		-Dargo_api_version=${ARGO_API_VERSION} \
		> openapi/paths.json

	@echo "Creating OpenAPI spec"
	jq -s '.[0] + .[1] + .[2] + .[3]' \
		openapi/custom/version.json \
		openapi/info.json \
		openapi/paths.json \
		openapi/definitions.json \
		> ${OPENAPI_SPEC}
	

preprocess:
	@echo "Preprocessing API specs"
	python scripts/preprocess.py -i ${OPENAPI_SPEC} \
		-d 'io.argoproj.workflow' \
		-o ${OPENAPI_SPEC} >/dev/null

	# Replace empty references
	sed -i -e '/"$$ref"/ s/io.argoproj.workflow.//' ${OPENAPI_SPEC}


client:
	@echo "Generating Argo ${ARGO_VERSION} client"

	CLIENT_VERSION=${CLIENT_VERSION} \
	KUBERNETES_BRANCH=${KUBERNETES_BRANCH} \
	PACKAGE_NAME=${PACKAGE_NAME} \
		./scripts/generate_client.sh ${OUTPUT_DIR} ${OPENAPI_SPEC} ${OPENAPI_CONFIG}

changelog:
	RELEASE_VERSION=${CLIENT_VERSION} ./scripts/generate_changelog.sh
