# Copyright 2019 Marek Cermak <macermak@redhat.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
A wrapper around kubernetes.config to set proper Argo ApiClient configuration
"""

import kubernetes
import mock

from argo.workflows.client import ApiClient, Configuration


def load_incluster_config():
    """See `kubernetes.config.load_incluset_config`."""
    with mock.patch('kubernetes.config.incluster_config.Configuration', Configuration):
        kubernetes.config.load_incluster_config()


load_incluster_config.__doc__ = kubernetes.config.load_incluster_config.__doc__


def load_kube_config(**kwargs):
    """See `kubernetes.config.load_kube_config`."""
    with mock.patch('kubernetes.config.kube_config.Configuration', Configuration):
        kubernetes.config.load_kube_config(**kwargs)


load_kube_config.__doc__ = kubernetes.config.load_kube_config.__doc__


def new_client_from_config(**kwargs):
    """See `kubernetes.config.new_client_from_config`."""
    with mock.patch.multiple(**{
        'kubernetes.config.kube_config.Configuration': Configuration,
        'kubernetes.config.kube_config.ApiClient': ApiClient
    }):
        kubernetes.new_client_from_config(**kwargs)


new_client_from_config.__doc__ = kubernetes.config.new_client_from_config.__doc__
