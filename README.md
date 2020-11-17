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

* [Argo Python DSL](https://github.com/argoproj-labs/argo-python-dsl) provides a pythonic workflow interface that can be extended to your specific needs (such as Data Science, ETL, etc)
* [Couler](https://github.com/couler-proj/couler) provides a simplified and unified interface for constructing and managing workflows

## Versioning

The client is generated from the Argo and Kubernetes OpenAPI specification.

We follow semantic versioning, the client starts at version `1.0` which matches Argo release `2.3.0` and continues onwards.

#### Current Version Mapping

Argo Python SDK: 3.6
Argo: 2.11.7
Kubernetes:

Key:

* `✓` Exactly the same features / API objects in both client-python and the Kubernetes
  version.
* `+` client-python has features or api objects that may not be present in the
  Kubernetes cluster, but everything they have in common will work.
* `-` The Kubernetes cluster has features the client-python library can't use
  (additional API objects, etc).

We try to be consistent with Argo as much as possible and hence we created special branches for user convenience --- for example [argo/v2.4.0](https://github.com/argoproj-labs/argo-client-python/tree/v2.10.2) is identical with Argo release [v2.10.2](https://github.com/argoproj/argo/releases/tag/v2.10.2).

These can be then installed directly from github:

```
pip install -e "git+https://github.com/argoproj-labs/argo-client-python.git@argo/v2.10.2#egg=argo-workflows"
```


## Code generation

The generated SDK will correspond to the argo version specified in the [ARGO_VERSION](./ARGO_VERSION) file.

If you wish to generate code yourself, you can do so by reproducing the build environment (image): `make builder_image`, then running `make builder_make` to generate the client.


#### Dependencies

Usually these will be kept up to date (or at least in sync in the branch named after the argo version that you are looking for)

- a compatible `KUBERNETES_BRANCH` according to Argo's [Gopkg.toml](https://github.com/argoproj/argo/blob/master/Gopkg.toml)
- a compatible version of [kubernetes-client](https://github.com/kubernetes-client/python#compatibility)
- [requirements.txt](./requirements.txt) and [Pipfile](Pipfile)

For additional configuration check out the [Makefile](./Makefile).
