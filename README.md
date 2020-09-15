# Argo Workflows Python Client

Python client for Argo Workflows

![](https://github.com/argoproj-labs/argo-client-python/workflows/CI/badge.svg)


## Installation

```bash
pip install argo-workflows
```

## Usage

If you're familiar with Kubernetes client, the Argo client follows the same behaviour.

```python
from argo.workflows.client import V1alpha1Api
from argo.workflows.config import load_kube_config

load_kube_config()  # loads local configuration from ~/.kube/config
```

And to list Workflows from a namespace (say `argo`):

```python
v1alpha1 = V1alpha1Api()

wfs = v1alpha1.list_namespaced_workflows(namespace="argo")
```

To submit a `Workflow`, one would simply load it from a YAML<sup>*</sup> and submit it as such:

```python
import requests
import yaml

namespace = "argo"

# hello-world example
resp = requests.get("https://raw.githubusercontent.com/argoproj/argo/master/examples/hello-world.yaml")
resp.raise_for_status()

manifest: dict = yaml.safe_load(resp.text)

# Submit the Workflow to the `argo` namespace
v1alpha1.create_namespaced_workflow(namespace, manifest)
```

When working on a higher level of abstraction, check out the following projects:

* [Couler](https://github.com/couler-proj/couler) that provides a simplified and unified interface for constructing and managing workflows
* [Argo Python DSL](https://github.com/CermakM/argo-python-dsl)

## Versioning

The client is generated from the Argo and Kubernetes OpenAPI specification.

We follow semantic versioning, the client starts at version `1.0` which matches Argo release `2.3.0` and continues onwards.

#### Compatibility matrix

|                    | Argo 2.3       | Argo 2.4        | Argo 2.5        |
|--------------------|----------------|-----------------|-----------------|
| client-python 1.0  |✓               |-                |-                |
| client-python 2.0  |+               |✓                |-                |
| client-python 3.0  |+               |+                |✓                |

Key:

* `✓` Exactly the same features / API objects in both client-python and the Kubernetes
  version.
* `+` client-python has features or api objects that may not be present in the
  Kubernetes cluster, but everything they have in common will work.
* `-` The Kubernetes cluster has features the client-python library can't use
  (additional API objects, etc).

We try to be consistent with Argo as much as possible and hence we created special branches for user convenience --- for example [argo/v2.4.0](https://github.com/CermakM/argo-client-python/tree/v2.4.0) is identical with Argo release [v2.4.0](https://github.com/argoproj/argo/releases/tag/v2.4.0).

These can be then installed directly from github:

```
pip install -e "git+git://github.com/CermakM/argo-client-python@argo/v2.4.0#egg=argo-workflows"
```

> :warning: The compatibility for such cases is not guaranteed


## Code generation

If you wish to generate code yourself, you can do so by running `make generate` with the `ARGO_VERSION` environment variable being set to the you want to generate the client for.

#### Before

in the Makefile:

- make sure to select a compatible `KUBERNETES_BRANCH` according to Argo's [Gopkg.toml](https://github.com/argoproj/argo/blob/master/Gopkg.toml)
- make sure to select a compatible version of [kubernetes-client](https://github.com/kubernetes-client/python#compatibility)
- update [requirements.txt](./requirements.txt) and [Pipfile](Pipfile)

For additional configuration check out the [Makefile](./Makefile).
