import requests
import pytest
import yaml
from . import create_workflow

NAMESPACE = "argo"
ARGO_VERSION = open("ARGO_VERSION").read()


DAG_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/workflow-template/dag.yaml'
HELLO_WORLD_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/workflow-template/hello-world.yaml'
STEPS_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/workflow-template/steps.yaml'
TEMPLATES_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/workflow-template/templates.yaml'
WORKFLOW_TEMPLATE_REF_WITH_ENTRY_POINT_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/workflow-template/workflow-template-ref-with-entrypoint-arg-passing.yaml'
WORKFLOW_TEMPLATE_REF_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/workflow-template/workflow-template-ref.yaml'


@pytest.fixture(scope="module")
def register_template_workflow():
    resp = requests.get(TEMPLATES_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflowtemplate(NAMESPACE, manifest)


def test_submit_dag_workflow():
    resp = requests.get(DAG_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_submit_hello_world_workflow():
    resp = requests.get(HELLO_WORLD_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_submit_steps_workflow():
    resp = requests.get(STEPS_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_submit_workflow_template_with_entry_arg():
    resp = requests.get(WORKFLOW_TEMPLATE_REF_WITH_ENTRY_POINT_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_submit_workflow_template_ref():
    resp = requests.get(WORKFLOW_TEMPLATE_REF_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)
