PACKAGE_NAME        = workflows.client
PACKAGE_DESCRIPTION = Python client for Argo Workflows

CURRENT_DIR ?= $(shell pwd)
OUTPUT_DIR  ?= ./

GIT_COMMIT     = $(shell git rev-parse HEAD)
GIT_TAG        = $(shell if [ -z "`git status --porcelain`" ]; then git describe --exact-match --tags HEAD 2>/dev/null; fi)
GIT_TREE_STATE = $(shell if [ -z "`git status --porcelain`" ]; then echo "clean" ; else echo "dirty"; fi)

ifeq (${GIT_TAG},)
GIT_TAG = $(shell git rev-parse --abbrev-ref HEAD)
endif

ARGO_VERSION      ?= ${GIT_TAG}
ARGO_API_GROUP    ?= argoproj.io
ARGO_API_VERSION  ?= v1alpha1
ARGO_OPENAPI_SPEC  = openapi/specs/argo-${ARGO_VERSION}.json

KUBERNETES_BRANCH      ?= release-1.14
KUBERNETES_OPENAPI_SPEC = openapi/specs/kubernetes-${KUBERNETES_BRANCH}.json

OPENAPI_SPEC   = openapi/swagger.json
OPENAPI_CONFIG = openapi/custom/config.json

CLIENT_VERSION = ${ARGO_VERSION}


.PHONY: all
all: generate

.PHONY: clean
clean:
	-rm -r openapi/specs/ ${OPENAPI_SPEC}
	-rm -r ${OUTPUT_DIR}/argo/workflows/client
	-rm -r ${OUTPUT_DIR}/docs/


spec: 
	# Make sure the folders exist
	mkdir -p openapi/specs/

	@echo "Collecting API spec for Argo ${ARGO_VERSION}"
	curl -sSL https://raw.githubusercontent.com/kubernetes/kubernetes/${KUBERNETES_BRANCH}/api/openapi-spec/swagger.json \
		-o ${KUBERNETES_OPENAPI_SPEC}
	
	@echo "Collecting API spec for Kubernetes ${KUBERNETES_BRANCH}"
	curl -sSL https://raw.githubusercontent.com/argoproj/argo/${ARGO_VERSION}/api/openapi-spec/swagger.json \
		-o ${ARGO_OPENAPI_SPEC}

	@echo "Extracting definitions"
	jq -r '{ definitions: .definitions }' ${ARGO_OPENAPI_SPEC} \
		> openapi/definitions/argo.json

	@echo "Merging API definitions"
	jq -sS '.[0] * .[1]' \
		openapi/definitions/argo.json \
		openapi/definitions/V1Time.json \
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


.PHONY: generate
generate: clean spec preprocess client
