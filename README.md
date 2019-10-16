# argo-client-python
Python client for Argo Workflows


## Installation

```bash
pip install argo
```

## Usage

If you're familiar with Kubernetes client, the Argo client follows the same behaviour.

```python
from argo.client import V1alpha1Api
from argo.config import load_kube_config

load_kube_config()  # loads local configuration from ~/.kube/config
```

And to list Workflows from a namespace (say `argo`):

```python
v1alpha1 = V1alpha1Api()

wfs = v1alpha1.list_namespaced_workflows(namespace="argo")
```

## Versioning

The whole client is generated from the Argo and Kubernetes OpenAPI specification. We are consistent with Argo versions and hence for example branch [@v2.4.0](https://github.com/CermakM/argo-client-python/tree/v2.4.0) is identical with Argo release [v2.4.0](https://github.com/argoproj/argo/releases/tag/v2.4.0).


## Code generation

If you wish to generate code yourself, you can do so by running `make generate` with the `ARGO_VERSION` environment variable being set to the you want to generate the client for.
For additional configuration check out the [Makefile](./Makefile).