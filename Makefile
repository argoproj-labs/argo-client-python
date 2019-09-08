PACKAGE_NAME        = client
PACKAGE_DESCRIPTION = Python client for Argo Workflows

CURRENT_DIR ?= $(shell pwd)
OUTPUT_DIR  ?= argo

GIT_COMMIT     = $(shell git rev-parse HEAD)
GIT_TAG        = $(shell if [ -z "`git status --porcelain`" ]; then git describe --exact-match --tags HEAD 2>/dev/null; fi)
GIT_TREE_STATE = $(shell if [ -z "`git status --porcelain`" ]; then echo "clean" ; else echo "dirty"; fi)

ifeq ($(shell echo $(realpath ${OUTPUT_DIR})), ${CURRENT_DIR})
$(error `OUTPUT_DIR` must not be the same as `CURRENT_DIR`)
endif

ifeq (${GIT_TAG},)
GIT_TAG = $(shell git rev-parse --abbrev-ref HEAD)
endif

ARGO_VERSION           ?= ${GIT_TAG}
ARGO_OPENAPI_SPEC       = openapi/specs/argo-${ARGO_VERSION}.json
KUBERNETES_BRANCH      ?= release-1.14
KUBERNETES_OPENAPI_SPEC = openapi/specs/kubernetes-${KUBERNETES_BRANCH}.json

OPENAPI_SPEC   = openapi/openapi.json
OPENAPI_CONFIG = openapi/config.json

CLIENT_VERSION = ${ARGO_VERSION}


.PHONY: all
all: generate

.PHONY: clean
clean:
	-rm -rf openapi/specs/ openapi/definitions/ ${OPENAPI_SPEC}
	-rm -rf ${OUTPUT_DIR}/${PACKAGE_NAME}


spec: 
	# Make sure the folders exist
	mkdir -p openapi/specs openapi/definitions

	@echo "Collecting API spec for Argo ${ARGO_VERSION}"
	curl -sSL https://raw.githubusercontent.com/kubernetes/kubernetes/${KUBERNETES_BRANCH}/api/openapi-spec/swagger.json \
		-o ${KUBERNETES_OPENAPI_SPEC}
	
	@echo "Collecting API spec for Kubernetes ${KUBERNETES_BRANCH}"
	curl -sSL https://raw.githubusercontent.com/argoproj/argo/${ARGO_VERSION}/api/openapi-spec/swagger.json \
		-o ${ARGO_OPENAPI_SPEC}

	@echo "Processing definitions"
	jq -r '{ definitions: .definitions }' ${ARGO_OPENAPI_SPEC} \
		> openapi/definitions/argo.json
	# jq -r '{ definitions: .definitions }' ${KUBERNETES_OPENAPI_SPEC} \
	# 	> openapi/definitions/kubernetes.json

	@echo "Merging API definitions"
	jq -sS '.[0] + .[1]' openapi/definitions/* \
		> openapi/definitions/definitions.json

	@echo "Creating OpenAPI info"
	echo '{"info": {"title": "Argo", "description": "${PACKAGE_DESCRIPTION}", "version": "${ARGO_VERSION}"}}' | jq \
		> openapi/custom/info.json

	@echo "Creating OpenAPI spec"
	jq -s '.[0] + .[1] + .[2] + .[3]' \
		openapi/custom/swagger.json \
		openapi/custom/info.json \
		openapi/custom/paths.json \
		openapi/definitions/definitions.json \
		> ${OPENAPI_SPEC}
	

preprocess:
	@echo "Preprocessing API specs"
	python scripts/preprocess.py -i ${OPENAPI_SPEC} \
		-d 'io.k8s' \
		-d 'io.argoproj.workflow' \
		-o ${OPENAPI_SPEC} >/dev/null


.PHONY: generate
generate: spec preprocess
	@echo "Generating Argo ${ARGO_VERSION} client"

	CLIENT_VERSION=${CLIENT_VERSION} \
	KUBERNETES_BRANCH=${KUBERNETES_BRANCH} \
	PACKAGE_NAME=${PACKAGE_NAME} \
		./scripts/generate_client.sh ${OUTPUT_DIR} ${OPENAPI_SPEC} ${OPENAPI_CONFIG}
