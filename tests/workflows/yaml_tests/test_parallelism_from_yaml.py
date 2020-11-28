import requests
import pytest
import yaml
from . import create_workflow

NAMESPACE = "argo"
ARGO_VERSION = open("ARGO_VERSION").read()


PARALLELISM_LIMIT_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/parallelism-limit.yaml'
PARALLELISM_NESTED_DAG_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/parallelism-nested-dag.yaml'
PARALLELISM_NESTED_WORKFLOW_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/parallelism-nested-workflow.yaml'
PARALLELISM_NESTED_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/parallelism-nested.yaml'
PARALLELSIM_TEMPLATE_LIMIT_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/parallelism-template-limit.yaml'
PARALLELISM_AGG_DAG_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/parameter-aggregation-dag.yaml'


def test_submit_parallelism_limit_workflow():
    resp = requests.get(PARALLELISM_LIMIT_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_submit_parallelism_nested_dag_workflow():
    resp = requests.get(PARALLELISM_NESTED_DAG_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_submit_parallelism_nested_wf_workflow():
    resp = requests.get(PARALLELISM_NESTED_WORKFLOW_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_submit_parallelism_nested_workflow():
    resp = requests.get(PARALLELISM_NESTED_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_submit_parallelism_agg_dag_workflow():
    resp = requests.get(PARALLELISM_AGG_DAG_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_submit_parallelism_template_limit_workflow():
    resp = requests.get(PARALLELSIM_TEMPLATE_LIMIT_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)
