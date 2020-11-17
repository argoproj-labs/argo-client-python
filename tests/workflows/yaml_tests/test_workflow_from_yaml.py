import requests
import yaml
from argo.workflows.client import V1alpha1Api
from argo.workflows.config import load_kube_config

NAMESPACE = "argo"
ARGO_VERSION = open("ARGO_VERSION").read()

load_kube_config()  # loads local configuration from ~/.kube/config

# Basic
HELLO_WORLD_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/hello-world.yaml'

# CRON
CRON_WORKFLOW_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/cron-workflow.yaml'

# Conditionals
CORN_FLIP_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/coinflip.yaml'

# Arguments
ARGUMENTS_ARTIFACT_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/arguments-artifacts.yaml'
ARGUMENTS_PARAMETERS_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/arguments-parameters.yaml'

# Artifacts
ARTIFACT_DISABLE_ARCHIVE_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/artifact-disable-archive.yaml'
ARTIFACT_PASSING_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/artifact-passing.yaml'
ARTIFACT_PASSING_SUBPATH_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/artifact-passing-subpath.yaml'
ARTIFACT_PATH_PLACEHOLDERS_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/artifact-path-placeholders.yaml'
ARTIFACT_REPO_REF_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/artifact-repository-ref.yaml'

# Dags
DAG_CORN_FLIP_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/dag-coinflip.yaml'
DAG_CONTINUE_ON_FAIL_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/dag-continue-on-fail.yaml'
DAG_DAEMON_TASK_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/dag-daemon-task.yaml'
DAG_DIAMOND_STEPS_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/dag-diamond-steps.yaml'
DAG_DIAMOND_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/dag-diamond.yaml'
DAG_DISABLE_FAILFAST_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/dag-disable-failFast.yaml'
DAG_ENHANCED_DEPENDS_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/dag-enhanced-depends.yaml'
DAG_MULTI_ROOT_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/dag-multiroot.yaml'
DAG_NESTED_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/dag-nested.yaml'
DAG_TARGETS_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/dag-targets.yaml'

# Exit handling
EXIT_CODE_OUTPUT_VARIABLE = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/exit-code-output-variable.yaml'
EXIT_HANDLER_DAG_LEVEL = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/exit-handler-dag-level.yaml'
EXIT_HANDLER_STEP_LEVEL = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/exit-handler-step-level.yaml'
EXIT_HANDLERS_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/exit-handlers.yaml'

# Global scopes
GLOBAL_OUTPUTS_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/global-outputs.yaml'
GLOBAL_PARAMETERS_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/global-parameters.yaml'

# Inputs
INPUTS_ARTIFACT_GCS_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/input-artifact-gcs.yaml'
INPUTS_ARTIFACT_GIT_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/input-artifact-git.yaml'
INPUTS_ARTIFACT_HTTP_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/input-artifact-http.yaml'
INPUTS_ARTIFACT_OSS_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/input-artifact-oss.yaml'
INPUTS_ARTIFACT_RAW_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/input-artifact-raw.yaml'
INPUTS_ARTIFACT_S3_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/input-artifact-s3.yaml'

# Loops
LOOPS_DAG_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/loops-dag.yaml'
LOOPS_MAP_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/loops-maps.yaml'
LOOPS_PARAM_ARGUMENT_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/loops-param-argument.yaml'
LOOPS_PARAM_RESULT_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/loops-param-result.yaml'
LOOPS_SEQUENCE_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/loops-sequence.yaml'
LOOPS_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/loops.yaml'

# Parameter aggregation
PARAMETER_AGGREGATION_SCRIPT_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/parameter-aggregation-script.yaml'
PARAMETER_AGGREGATION_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/parameter-aggregation.yaml'

# Scripts
SCRIPTS_BASH_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/scripts-bash.yaml'
SCRIPTS_PYTHON_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/scripts-python.yaml'
SCRIPTS_JAVASCRIPT_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/scripts-javascript.yaml'


def test_submit_hello_world_workflow():
    resp = requests.get(HELLO_WORLD_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_cron_workflow():
    resp = requests.get(CRON_WORKFLOW_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    # NOTE: avoid name collision while running the tests multiple times without clearing the database
    del manifest['metadata']['name']
    manifest['metadata']['generateName'] = f'cron-workflow-'
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_cronworkflow(NAMESPACE, manifest)


def test_submit_corn_flip_workflow():
    resp = requests.get(CORN_FLIP_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_argument_artifact_workflow():
    resp = requests.get(ARGUMENTS_ARTIFACT_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_argument_parameters_workflow():
    resp = requests.get(ARGUMENTS_PARAMETERS_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_artifact_disable_archive_workflow():
    resp = requests.get(ARTIFACT_DISABLE_ARCHIVE_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_artifact_passing_workflow():
    resp = requests.get(ARTIFACT_PASSING_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)

def test_submit_artifact_passing_subpath_workflow():
    resp = requests.get(ARTIFACT_PASSING_SUBPATH_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_artifact_path_placeholders_workflow():
    resp = requests.get(ARTIFACT_PATH_PLACEHOLDERS_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_artifact_repo_ref_workflow():
    resp = requests.get(ARTIFACT_REPO_REF_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_dag_corn_flip_workflow():
    resp = requests.get(DAG_CORN_FLIP_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_dag_continue_on_fail_workflow():
    resp = requests.get(DAG_CONTINUE_ON_FAIL_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_dag_daemon_task_workflow():
    resp = requests.get(DAG_DAEMON_TASK_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_dag_diamond_steps_workflow():
    resp = requests.get(DAG_DIAMOND_STEPS_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_dag_diamond_workflow():
    resp = requests.get(DAG_DIAMOND_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_dag_disable_failfast_workflow():
    resp = requests.get(DAG_DISABLE_FAILFAST_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_dag_enhanced_depends_workflow():
    resp = requests.get(DAG_ENHANCED_DEPENDS_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_dag_multi_root_workflow():
    resp = requests.get(DAG_MULTI_ROOT_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_dag_nested_workflow():
    resp = requests.get(DAG_NESTED_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_dag_targets_workflow():
    resp = requests.get(DAG_TARGETS_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_exit_code_output_variable_workflow():
    resp = requests.get(EXIT_CODE_OUTPUT_VARIABLE)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_exit_handler_dag_level_workflow():
    resp = requests.get(EXIT_CODE_OUTPUT_VARIABLE)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_exit_handler_step_level_workflow():
    resp = requests.get(EXIT_HANDLER_STEP_LEVEL)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_exit_handler_step_level_workflow():
    resp = requests.get(EXIT_HANDLERS_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_global_outputs_workflow():
    resp = requests.get(GLOBAL_OUTPUTS_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_global_parameters_workflow():
    resp = requests.get(GLOBAL_PARAMETERS_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_input_artifact_gcs_workflow():
    resp = requests.get(INPUTS_ARTIFACT_GCS_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_input_artifact_git_workflow():
    resp = requests.get(INPUTS_ARTIFACT_GIT_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_input_artifact_http_workflow():
    resp = requests.get(INPUTS_ARTIFACT_HTTP_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_input_artifact_oss_workflow():
    resp = requests.get(INPUTS_ARTIFACT_OSS_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_input_artifact_raw_workflow():
    resp = requests.get(INPUTS_ARTIFACT_RAW_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_input_artifact_s3_workflow():
    resp = requests.get(INPUTS_ARTIFACT_S3_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_loops_dag_workflow():
    resp = requests.get(LOOPS_DAG_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_loops_map_workflow():
    resp = requests.get(LOOPS_MAP_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_loops_param_argument_workflow():
    resp = requests.get(LOOPS_PARAM_ARGUMENT_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_loops_param_result_workflow():
    resp = requests.get(LOOPS_PARAM_RESULT_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_loops_sequence_workflow():
    resp = requests.get(LOOPS_SEQUENCE_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_loops_workflow():
    resp = requests.get(LOOPS_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_parameter_aggregation_script_workflow():
    resp = requests.get(PARAMETER_AGGREGATION_SCRIPT_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_parameter_aggregation_workflow():
    resp = requests.get(PARAMETER_AGGREGATION_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_script_bash_workflow():
    resp = requests.get(SCRIPTS_BASH_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_script_javascript_workflow():
    resp = requests.get(SCRIPTS_JAVASCRIPT_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_script_python_workflow():
    resp = requests.get(SCRIPTS_PYTHON_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)
