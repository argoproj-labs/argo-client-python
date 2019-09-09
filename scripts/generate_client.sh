#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail


# Cleanup generated code.
# args:
#   $1: output directory
_cleanup() {
    local output_dir="$1"

    echo "Cleanup."
	# Replace io.k8s models with python kubernetes client library
	find $output_dir -type f -exec \
		sed -i 's/IoK8sApiCore\|IoK8sApimachineryPkgApisMeta/kubernetes.client./g' {} \;

    mv $output_dir/${PACKAGE_NAME}_README.md $output_dir/README.md
}

# Generates client.
# args:
#   $1: output directory
#   $2: path to openaAPI specifiaction
#   $2: path to openaAPI config
# env:
#   [required] CLIENT_VERSION   : Client version. Will be used in the comment sections of the generated code
#   [required] PACKAGE_NAME     : Name of the client package.
#   [required] KUBERNETES_BRANCH: Kubernetes branch name to get the swagger spec from
argo::generate::generate_client() {
    : "${CLIENT_VERSION?Must set CLIENT_VERSION env var}"
    : "${KUBERNETES_BRANCH?Must set KUBERNETES_BRANCH env var}"
    : "${PACKAGE_NAME?Must set PACKAGE_NAME env var}"

    local output_dir="$1"
    local openapi_spec="$2"
    local openapi_config="$3"

    mkdir -p $output_dir
	docker run --rm -v ${PWD}:/local:Z openapitools/openapi-generator-cli generate \
		-g python \
		-c /local/${openapi_config} \
		-i /local/${openapi_spec} \
		-o /local/${output_dir} \
		-p packageName=${PACKAGE_NAME} \
		-p packageVersion=${CLIENT_VERSION}
    
    _cleanup $output_dir
}

args=("$@")

if [ "$0" = "$BASH_SOURCE" ] ; then
    argo::generate::generate_client ${args[@]}
fi
