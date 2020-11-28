import requests
import pytest
import yaml
from . import create_workflow

NAMESPACE = "argo"
ARGO_VERSION = open("ARGO_VERSION").read()


POD_SPEC_YAML_PATCH_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/pod-spec-yaml-patch.yaml'
POD_SPEC_PATCH_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/pod-spec-patch.yaml'
POD_SPEC_PATCH_WF_TMPL_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/pod-spec-patch-wf-tmpl.yaml'
POD_SPEC_FROM_PREV_STEP_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/pod-spec-from-previous-step.yaml'
POD_METADATA_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/pod-metadata.yaml'
POD_GC_STRATEGY_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/pod-gc-strategy.yaml'
INIT_CONTAINER_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/init-container.yaml'
IMAGE_PULL_SECRETS = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/image-pull-secrets.yaml'


def test_pod_spec_yaml_patch_workflow():
    resp = requests.get(POD_SPEC_YAML_PATCH_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_pod_spec_patch_workflow():
    resp = requests.get(POD_SPEC_PATCH_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_pod_spec_patch_wf_tmpl_workflow():
    resp = requests.get(POD_SPEC_PATCH_WF_TMPL_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_pod_spec_from_prev_step_workflow():
    resp = requests.get(POD_SPEC_FROM_PREV_STEP_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_pod_gc_strategy_workflow():
    resp = requests.get(POD_GC_STRATEGY_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_init_container_workflow():
    resp = requests.get(INIT_CONTAINER_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_image_pull_secrets_workflow():
    resp = requests.get(IMAGE_PULL_SECRETS)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)
