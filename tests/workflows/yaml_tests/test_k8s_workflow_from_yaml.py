import requests
import pytest
import yaml
from argo.workflows.client import V1alpha1Api
from argo.workflows.config import load_kube_config

NAMESPACE = "argo"
ARGO_VERSION = open("ARGO_VERSION").read()

load_kube_config()  # loads local configuration from ~/.kube/config

K8S_JOBS_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/k8s-jobs.yaml'
K8S_ORCHESTRATION_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/k8s-orchestration.yaml'
K8S_OWNER_REFERENCE_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/k8s-owner-reference.yaml'
K8S_SET_OWNER_REFERENCE_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/k8s-set-owner-reference.yaml'
K8S_WAIT_WF_YML = f'https://raw.githubusercontent.com/argoproj/argo/v{ARGO_VERSION}/examples/k8s-wait-wf.yaml'


def test_submit_k8s_jobs_workflow():
    resp = requests.get(K8S_JOBS_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_k8s_orchestration_workflow():
    resp = requests.get(K8S_ORCHESTRATION_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_k8s_owner_reference_workflow():
    resp = requests.get(K8S_OWNER_REFERENCE_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_k8s_orchestration_workflow():
    resp = requests.get(K8S_ORCHESTRATION_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_k8s_set_owner_reference_workflow():
    resp = requests.get(K8S_SET_OWNER_REFERENCE_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)


def test_submit_k8s_wait_wf_workflow():
    resp = requests.get(K8S_WAIT_WF_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)
