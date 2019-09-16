#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail


# Patch generated code.
# args:
#   $1: output directory
_patch() {
    local output_dir="$1"

    echo "--- Patching generated code..."

    # Fix issue with Swagger not respecting Python subpackages
    cp -rl ${output_dir}/${PACKAGE_NAME}/* "${output_dir}/${PACKAGE_NAME//[.]/\/}/" ; rm -r ${output_dir}/${PACKAGE_NAME}

	# Replace io.k8s models with python kubernetes.client.library
    find "$output_dir/${PACKAGE_NAME//[.]/\/}/" -type f \
        -exec sed -i "/import IoK8s/d" {} \; \
        -exec sed -i "s/IoK8sApiCore\|IoK8sApimachineryPkgApisMeta//g" {} \;
    
    py_models="$output_dir/${PACKAGE_NAME//[.]/\/}/models/__init__.py" ; echo >> $py_models
    
    # Import kubernetes to the relevant files
    declare -A models
    find "$output_dir/${PACKAGE_NAME//[.]/\/}/" ! -path '*/__pycache__/*' -type f | while read fname; do
    {
        set +o pipefail

        ln=$(grep -P "V1(?!alpha)" ${fname} >/dev/null && grep -n "import" ${fname} | tail -n1 | awk '{print $1}' FS=":" || true)
        if [ ! -z "${ln}" ]; then
            let ln++

            grep -P 'V1(?!alpha)[a-zA-Z]+' -oh ${fname} | sort -u | while read model; do
                let ln++
                sed -i "${ln}i from kubernetes.client.models import ${model}" ${fname}
                {
                    set +o nounset; if [ -z "${models[$model]}" ]; then
                        sed -i "\$a from kubernetes.client.models import ${model}" ${py_models}
                    fi
                }
                models[${model}]=1
            done
        fi
    }
    done

    echo "--- Done."
}

# Cleanup generated code.
# args:
#   $1: output directory
_cleanup() {
    local output_dir="$1"

    echo "--- Cleanup."
    {
        set +o nounset;
        [ ! -z ${CLEANUP_DIRS} ] && rm -r ${CLEANUP_DIRS}
    }

    echo "--- Done."
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

    echo "--- Generating client."

    local output_dir="$1"
    local openapi_spec="$2"
    local openapi_config="$3"

    mkdir -m 755 -p $output_dir
	docker run --user ${UID} --rm -v ${PWD}:/local:z swaggerapi/swagger-codegen-cli generate \
		-l python \
		-c /local/${openapi_config} \
		-i /local/${openapi_spec} \
		-o /local/${output_dir} \
        -DmodelTests=false \
		-DpackageName=${PACKAGE_NAME} \
		-DpackageVersion=${CLIENT_VERSION}
    
    CLEANUP_DIRS=( "${output_dir}/test" )
    
    _patch   $output_dir
    _cleanup $output_dir

    echo "--- Done."
}

args=("$@")

if [ "$0" = "$BASH_SOURCE" ] ; then
    argo::generate::generate_client ${args[@]}
fi
