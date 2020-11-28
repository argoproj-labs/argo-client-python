import requests
import pytest
import yaml
from . import create_workflow

NAMESPACE = "argo"
ARGO_VERSION = open("ARGO_VERSION").read()


RESUBMIT_WORKFLOW_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/resubmit.yaml'
RETRY_BACKOFF_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/retry-backoff.yaml'
RETRY_CONTAINER_TO_COMPLETION_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/retry-container-to-completion.yaml'
RETRY_CONTAINER_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/retry-container.yaml'
RETRY_ON_ERROR_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/retry-on-error.yaml'
RETRY_SCRIPT_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/retry-script.yaml'
RETRY_WITH_STEPS_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/retry-with-steps.yaml'


def test_resubmit_workflow():
    resp = requests.get(RESUBMIT_WORKFLOW_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_retry_backoff_workflow():
    resp = requests.get(RETRY_BACKOFF_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_retry_container_to_completion_workflow():
    resp = requests.get(RETRY_CONTAINER_TO_COMPLETION_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_submit_retry_with_steps_workflow():
    resp = requests.get(RETRY_WITH_STEPS_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_retry_script_workflow():
    resp = requests.get(RETRY_SCRIPT_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_retry_on_error_workflow():
    resp = requests.get(RETRY_ON_ERROR_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)
