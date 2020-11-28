import requests
import yaml
from . import create_workflow

NAMESPACE = "argo"
ARGO_VERSION = open("ARGO_VERSION").read()


SYNCHRONIZATION_WF_LEVEL_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/synchronization-wf-level.yaml'

SYNCHRONIZATION_TMPL_LEVEL_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/synchronization-tmpl-level.yaml'

SYNCHRONIZATION_MUTEX_WF_LEVEL_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/synchronization-mutex-wf-level.yaml'

SYNCHRONIZATION_MUTEX_TMPL_LEVEL_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/synchronization-mutex-tmpl-level.yaml'


def test_submit_synchronization_wf_level_workflow():
    resp = requests.get(SYNCHRONIZATION_WF_LEVEL_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_submit_synchronization_tmpl_level_workflow():
    resp = requests.get(SYNCHRONIZATION_TMPL_LEVEL_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_submit_synchronization_mutex_wf_level_workflow():
    resp = requests.get(SYNCHRONIZATION_MUTEX_WF_LEVEL_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)


def test_submit_synchronization_mutex_wf_tmpl_level_workflow():
    resp = requests.get(SYNCHRONIZATION_MUTEX_TMPL_LEVEL_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)

    create_workflow(NAMESPACE, manifest)
