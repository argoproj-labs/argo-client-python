"""Python client for Argo Workflows."""

from argo.workflows import client
from argo.workflows import config
from argo.workflows import watch

from argo.workflows.client import models

from argo.workflows.client.__about__ import __version__ as __client_version__
