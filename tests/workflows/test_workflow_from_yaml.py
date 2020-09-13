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
DAG_CONTINUE_ON_FAIL = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/dag-continue-on-fail.yaml'
DAG_DAEMON_TASK = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/dag-daemon-task.yaml'
DAG_DIAMOND_STEPS = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/dag-diamond-steps.yaml'
DAG_DIAMOND = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/dag-diamond.yaml'
DAG_DISABLE_FAILFAST = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/dag-disable-failFast.yaml'
DAG_ENHANCED_DEPENDS = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/dag-enhanced-depends.yaml'
DAG_MULTI_ROOT = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/dag-multiroot.yaml'
DAG_NESTED = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/dag-nested.yaml'
DAG_TARGETS = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/dag-targets.yaml'

# Exit handling
EXIT_CODE_OUTPUT_VARIABLE = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/exit-code-output-variable.yaml'


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
    resp = requests.get(DAG_CONTINUE_ON_FAIL)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_dag_daemon_task_workflow():
    resp = requests.get(DAG_DAEMON_TASK)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_dag_diamond_steps_workflow():
    resp = requests.get(DAG_DIAMOND_STEPS)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_dag_diamond_workflow():
    resp = requests.get(DAG_DIAMOND)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_dag_disable_failfast_workflow():
    resp = requests.get(DAG_DISABLE_FAILFAST)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_dag_enhanced_depends_workflow():
    resp = requests.get(DAG_ENHANCED_DEPENDS)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_dag_multi_root_workflow():
    resp = requests.get(DAG_MULTI_ROOT)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_dag_nested_workflow():
    resp = requests.get(DAG_NESTED)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_dag_targets_workflow():
    resp = requests.get(DAG_TARGETS)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)
