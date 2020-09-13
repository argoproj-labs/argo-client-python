import requests
import yaml
from argo.workflows.client import V1alpha1Api
from argo.workflows.config import load_kube_config

NAMESPACE = "argo"

load_kube_config()  # loads local configuration from ~/.kube/config

# Basic
HELLO_WORLD_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/hello-world.yaml'

# CRON
CRON_WORKFLOW_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/cron-workflow.yaml'

# Conditionals
CORN_FLIP_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/coinflip.yaml'

# Arguments
ARGUMENTS_ARTIFACT_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/arguments-artifacts.yaml'
ARGUMENTS_PARAMETERS_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/arguments-parameters.yaml'

# Artifacts
ARTIFACT_DISABLE_ARCHIVE_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/artifact-disable-archive.yaml'
ARTIFACT_PASSING_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/artifact-passing.yaml'
ARTIFACT_PATH_PLACEHOLDERS_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/artifact-path-placeholders.yaml'
ARTIFACT_REPO_REF_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/artifact-repository-ref.yaml'

# Dags
DAG_CORN_FLIP_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/dag-coinflip.yaml'
DAG_CONTINUE_ON_FAIL_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/dag-continue-on-fail.yaml'
DAG_DAEMON_TASK_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/dag-daemon-task.yaml'
DAG_DIAMOND_STEPS_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/dag-diamond-steps.yaml'
DAG_DIAMOND_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/dag-diamond.yaml'
DAG_DISABLE_FAILFAST_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/dag-disable-failFast.yaml'
DAG_ENHANCED_DEPENDS_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/dag-enhanced-depends.yaml'
DAG_MULTI_ROOT_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/dag-multiroot.yaml'
DAG_NESTED_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/dag-nested.yaml'
DAG_TARGETS_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/dag-targets.yaml'

# Exit handling
EXIT_CODE_OUTPUT_VARIABLE = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/exit-code-output-variable.yaml'
EXIT_HANDLER_DAG_LEVEL = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/exit-handler-dag-level.yaml'
EXIT_HANDLER_STEP_LEVEL = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/exit-handler-step-level.yaml'
EXIT_HANDLERS_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/exit-handlers.yaml'

# Global scopes
GLOBAL_OUTPUTS_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/global-outputs.yaml'
GLOBAL_PARAMETERS_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/global-parameters.yaml'

# Inputs
INPUTS_ARTIFACT_GCS_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/input-artifact-gcs.yaml'
INPUTS_ARTIFACT_GIT_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/input-artifact-git.yaml'
INPUTS_ARTIFACT_HTTP_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/input-artifact-http.yaml'
INPUTS_ARTIFACT_OSS_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/input-artifact-oss.yaml'
INPUTS_ARTIFACT_RAW_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/input-artifact-raw.yaml'
INPUTS_ARTIFACT_S3_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/input-artifact-s3.yaml'

# Loops
LOOPS_DAG_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/loops-dag.yaml'
LOOPS_MAP_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/loops-maps.yaml'
LOOPS_PARAM_ARGUMENT_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/loops-param-argument.yaml'
LOOPS_PARAM_RESULT_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/loops-param-result.yaml'
LOOPS_SEQUENCE_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/loops-sequence.yaml'
LOOPS_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/loops.yaml'


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
    manifest['metadata']['generateName'] = 'cron-workflow-'
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
