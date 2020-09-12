import requests
import yaml
from argo.workflows.client import V1alpha1Api
from argo.workflows.config import load_kube_config

NAMESPACE = "argo"

load_kube_config()  # loads local configuration from ~/.kube/config



# hello-world example



HELLO_WORLD_YML = 'https://raw.githubusercontent.com/argoproj/argo/v2.10.1/examples/hello-world.yaml'

def test_submit_hello_world_workflow():
    resp = requests.get(HELLO_WORLD_YML)
    resp.raise_for_status()

    manifest: dict = yaml.safe_load(resp.text)
    v1alpha1 = V1alpha1Api()
    # Submit the Workflow to the `argo` namespace
    v1alpha1.create_namespaced_workflow(NAMESPACE, manifest)
