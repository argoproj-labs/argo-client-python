# openapi_client.V1alpha1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_namespaced_archivedworkflow**](V1alpha1Api.md#create_namespaced_archivedworkflow) | **POST** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/archivedarchivedworkflows | 
[**create_namespaced_cronworkflow**](V1alpha1Api.md#create_namespaced_cronworkflow) | **POST** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/croncronworkflows | 
[**create_namespaced_workflow**](V1alpha1Api.md#create_namespaced_workflow) | **POST** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/workflows | 
[**create_namespaced_workflowtemplate**](V1alpha1Api.md#create_namespaced_workflowtemplate) | **POST** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/workflowtemplates | 
[**delete_namespaced_archivedworkflow**](V1alpha1Api.md#delete_namespaced_archivedworkflow) | **DELETE** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/archivedarchivedworkflows/{name} | 
[**delete_namespaced_cronworkflow**](V1alpha1Api.md#delete_namespaced_cronworkflow) | **DELETE** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/croncronworkflows/{name} | 
[**delete_namespaced_workflow**](V1alpha1Api.md#delete_namespaced_workflow) | **DELETE** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/workflows/{name} | 
[**delete_namespaced_workflowtemplate**](V1alpha1Api.md#delete_namespaced_workflowtemplate) | **DELETE** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/workflowtemplates/{name} | 
[**get_namespaced_archivedworkflow**](V1alpha1Api.md#get_namespaced_archivedworkflow) | **GET** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/archivedarchivedworkflows/{name} | 
[**get_namespaced_cronworkflow**](V1alpha1Api.md#get_namespaced_cronworkflow) | **GET** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/croncronworkflows/{name} | 
[**get_namespaced_workflow**](V1alpha1Api.md#get_namespaced_workflow) | **GET** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/workflows/{name} | 
[**get_namespaced_workflowtemplate**](V1alpha1Api.md#get_namespaced_workflowtemplate) | **GET** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/workflowtemplates/{name} | 
[**list_namespaced_archivedworkflows**](V1alpha1Api.md#list_namespaced_archivedworkflows) | **GET** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/archivedarchivedworkflows | 
[**list_namespaced_cronworkflows**](V1alpha1Api.md#list_namespaced_cronworkflows) | **GET** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/croncronworkflows | 
[**list_namespaced_workflows**](V1alpha1Api.md#list_namespaced_workflows) | **GET** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/workflows | 
[**list_namespaced_workflowtemplates**](V1alpha1Api.md#list_namespaced_workflowtemplates) | **GET** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/workflowtemplates | 
[**patch_namespaced_archivedworkflow**](V1alpha1Api.md#patch_namespaced_archivedworkflow) | **PATCH** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/archivedarchivedworkflows/{name} | 
[**patch_namespaced_cronworkflow**](V1alpha1Api.md#patch_namespaced_cronworkflow) | **PATCH** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/croncronworkflows/{name} | 
[**patch_namespaced_workflow**](V1alpha1Api.md#patch_namespaced_workflow) | **PATCH** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/workflows/{name} | 
[**patch_namespaced_workflowtemplate**](V1alpha1Api.md#patch_namespaced_workflowtemplate) | **PATCH** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/workflowtemplates/{name} | 
[**replace_namespaced_archivedworkflow**](V1alpha1Api.md#replace_namespaced_archivedworkflow) | **PUT** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/archivedarchivedworkflows/{name} | 
[**replace_namespaced_cronworkflow**](V1alpha1Api.md#replace_namespaced_cronworkflow) | **PUT** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/croncronworkflows/{name} | 
[**replace_namespaced_workflow**](V1alpha1Api.md#replace_namespaced_workflow) | **PUT** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/workflows/{name} | 
[**replace_namespaced_workflowtemplate**](V1alpha1Api.md#replace_namespaced_workflowtemplate) | **PUT** /apis/argoproj.io/v1alpha1/namespaces/{namespace}/workflowtemplates/{name} | 


# **create_namespaced_archivedworkflow**
> IoArgoprojArchivedworkflowV1alpha1Workflow create_namespaced_archivedworkflow(namespace, body)



Creates a namespace scoped Workflow

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The Workflow's namespace
body = openapi_client.IoArgoprojArchivedworkflowV1alpha1Workflow() # IoArgoprojArchivedworkflowV1alpha1Workflow | The JSON schema of the Workflow to create.

    try:
        api_response = api_instance.create_namespaced_archivedworkflow(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->create_namespaced_archivedworkflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The Workflow&#39;s namespace | 
 **body** | **IoArgoprojArchivedworkflowV1alpha1Workflow**| The JSON schema of the Workflow to create. | 

### Return type

[**IoArgoprojArchivedworkflowV1alpha1Workflow**](IoArgoprojArchivedworkflowV1alpha1Workflow.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_cronworkflow**
> IoArgoprojCronworkflowV1alpha1Workflow create_namespaced_cronworkflow(namespace, body)



Creates a namespace scoped Workflow

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The Workflow's namespace
body = openapi_client.IoArgoprojCronworkflowV1alpha1Workflow() # IoArgoprojCronworkflowV1alpha1Workflow | The JSON schema of the Workflow to create.

    try:
        api_response = api_instance.create_namespaced_cronworkflow(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->create_namespaced_cronworkflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The Workflow&#39;s namespace | 
 **body** | **IoArgoprojCronworkflowV1alpha1Workflow**| The JSON schema of the Workflow to create. | 

### Return type

[**IoArgoprojCronworkflowV1alpha1Workflow**](IoArgoprojCronworkflowV1alpha1Workflow.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_workflow**
> V1alpha1Workflow create_namespaced_workflow(namespace, body)



Creates a namespace scoped Workflow

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The Workflow's namespace
body = openapi_client.V1alpha1Workflow() # V1alpha1Workflow | The JSON schema of the Workflow to create.

    try:
        api_response = api_instance.create_namespaced_workflow(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->create_namespaced_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The Workflow&#39;s namespace | 
 **body** | [**V1alpha1Workflow**](V1alpha1Workflow.md)| The JSON schema of the Workflow to create. | 

### Return type

[**V1alpha1Workflow**](V1alpha1Workflow.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_workflowtemplate**
> V1alpha1WorkflowTemplate create_namespaced_workflowtemplate(namespace, body)



Creates a namespace scoped WorkflowTemplate

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The WorkflowTemplate's namespace
body = openapi_client.V1alpha1WorkflowTemplate() # V1alpha1WorkflowTemplate | The JSON schema of the WorkflowTemplate to create.

    try:
        api_response = api_instance.create_namespaced_workflowtemplate(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->create_namespaced_workflowtemplate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The WorkflowTemplate&#39;s namespace | 
 **body** | [**V1alpha1WorkflowTemplate**](V1alpha1WorkflowTemplate.md)| The JSON schema of the WorkflowTemplate to create. | 

### Return type

[**V1alpha1WorkflowTemplate**](V1alpha1WorkflowTemplate.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_archivedworkflow**
> object delete_namespaced_archivedworkflow(namespace, name, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)



Deletes the specified namespace scoped Workflow.

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The custom resource's namespace
name = 'name_example' # str | Unique Workflow name
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = True # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)
body = openapi_client.V1DeleteOptions() # V1DeleteOptions | Delete options to be send along in the body of this request. (optional)

    try:
        api_response = api_instance.delete_namespaced_archivedworkflow(namespace, name, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->delete_namespaced_archivedworkflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **name** | **str**| Unique Workflow name | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. | [optional] 
 **body** | **V1DeleteOptions**| Delete options to be send along in the body of this request. | [optional] 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_cronworkflow**
> object delete_namespaced_cronworkflow(namespace, name, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)



Deletes the specified namespace scoped Workflow.

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The custom resource's namespace
name = 'name_example' # str | Unique Workflow name
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = True # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)
body = openapi_client.V1DeleteOptions() # V1DeleteOptions | Delete options to be send along in the body of this request. (optional)

    try:
        api_response = api_instance.delete_namespaced_cronworkflow(namespace, name, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->delete_namespaced_cronworkflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **name** | **str**| Unique Workflow name | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. | [optional] 
 **body** | **V1DeleteOptions**| Delete options to be send along in the body of this request. | [optional] 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_workflow**
> object delete_namespaced_workflow(namespace, name, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)



Deletes the specified namespace scoped Workflow.

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The custom resource's namespace
name = 'name_example' # str | Unique Workflow name
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = True # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)
body = openapi_client.V1DeleteOptions() # V1DeleteOptions | Delete options to be send along in the body of this request. (optional)

    try:
        api_response = api_instance.delete_namespaced_workflow(namespace, name, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->delete_namespaced_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **name** | **str**| Unique Workflow name | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. | [optional] 
 **body** | **V1DeleteOptions**| Delete options to be send along in the body of this request. | [optional] 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_workflowtemplate**
> object delete_namespaced_workflowtemplate(namespace, name, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)



Deletes the specified namespace scoped WorkflowTemplate.

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The custom resource's namespace
name = 'name_example' # str | Unique WorkflowTemplate name
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = True # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)
body = openapi_client.V1DeleteOptions() # V1DeleteOptions | Delete options to be send along in the body of this request. (optional)

    try:
        api_response = api_instance.delete_namespaced_workflowtemplate(namespace, name, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->delete_namespaced_workflowtemplate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **name** | **str**| Unique WorkflowTemplate name | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. | [optional] 
 **body** | **V1DeleteOptions**| Delete options to be send along in the body of this request. | [optional] 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_archivedworkflow**
> IoArgoprojArchivedworkflowV1alpha1Workflow get_namespaced_archivedworkflow(namespace, name)



Get Workflow resource by the archivedworkflow name

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The custom resource's namespace
name = 'name_example' # str | Unique Workflow name

    try:
        api_response = api_instance.get_namespaced_archivedworkflow(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->get_namespaced_archivedworkflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **name** | **str**| Unique Workflow name | 

### Return type

[**IoArgoprojArchivedworkflowV1alpha1Workflow**](IoArgoprojArchivedworkflowV1alpha1Workflow.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_cronworkflow**
> IoArgoprojCronworkflowV1alpha1Workflow get_namespaced_cronworkflow(namespace, name)



Get Workflow resource by the cronworkflow name

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The custom resource's namespace
name = 'name_example' # str | Unique Workflow name

    try:
        api_response = api_instance.get_namespaced_cronworkflow(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->get_namespaced_cronworkflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **name** | **str**| Unique Workflow name | 

### Return type

[**IoArgoprojCronworkflowV1alpha1Workflow**](IoArgoprojCronworkflowV1alpha1Workflow.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_workflow**
> V1alpha1Workflow get_namespaced_workflow(namespace, name)



Get Workflow resource by the workflow name

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The custom resource's namespace
name = 'name_example' # str | Unique Workflow name

    try:
        api_response = api_instance.get_namespaced_workflow(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->get_namespaced_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **name** | **str**| Unique Workflow name | 

### Return type

[**V1alpha1Workflow**](V1alpha1Workflow.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_workflowtemplate**
> V1alpha1WorkflowTemplate get_namespaced_workflowtemplate(namespace, name)



Get WorkflowTemplate resource by its name

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The custom resource's namespace
name = 'name_example' # str | Unique WorkflowTemplate name

    try:
        api_response = api_instance.get_namespaced_workflowtemplate(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->get_namespaced_workflowtemplate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **name** | **str**| Unique WorkflowTemplate name | 

### Return type

[**V1alpha1WorkflowTemplate**](V1alpha1WorkflowTemplate.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_archivedworkflows**
> IoArgoprojArchivedworkflowV1alpha1WorkflowList list_namespaced_archivedworkflows(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



List archivedworkflow resources.

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The Workflow's namespace
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
watch = True # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. (optional)

    try:
        api_response = api_instance.list_namespaced_archivedworkflows(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->list_namespaced_archivedworkflows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The Workflow&#39;s namespace | 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. | [optional] 

### Return type

[**IoArgoprojArchivedworkflowV1alpha1WorkflowList**](IoArgoprojArchivedworkflowV1alpha1WorkflowList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;stream=watch

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_cronworkflows**
> IoArgoprojCronworkflowV1alpha1WorkflowList list_namespaced_cronworkflows(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



List cronworkflow resources.

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The Workflow's namespace
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
watch = True # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. (optional)

    try:
        api_response = api_instance.list_namespaced_cronworkflows(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->list_namespaced_cronworkflows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The Workflow&#39;s namespace | 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. | [optional] 

### Return type

[**IoArgoprojCronworkflowV1alpha1WorkflowList**](IoArgoprojCronworkflowV1alpha1WorkflowList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;stream=watch

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_workflows**
> V1alpha1WorkflowList list_namespaced_workflows(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



List workflow resources.

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The Workflow's namespace
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
watch = True # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. (optional)

    try:
        api_response = api_instance.list_namespaced_workflows(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->list_namespaced_workflows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The Workflow&#39;s namespace | 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. | [optional] 

### Return type

[**V1alpha1WorkflowList**](V1alpha1WorkflowList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;stream=watch

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_workflowtemplates**
> V1alpha1WorkflowTemplateList list_namespaced_workflowtemplates(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



List WorkflowTemplate resources.

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The WorkflowTemplate's namespace
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
watch = True # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. (optional)

    try:
        api_response = api_instance.list_namespaced_workflowtemplates(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->list_namespaced_workflowtemplates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The WorkflowTemplate&#39;s namespace | 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. | [optional] 

### Return type

[**V1alpha1WorkflowTemplateList**](V1alpha1WorkflowTemplateList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;stream=watch

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_archivedworkflow**
> object patch_namespaced_archivedworkflow(namespace, name, body)



patch the specified namespace scoped Workflow.

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The custom resource's namespace
name = 'name_example' # str | Unique Workflow name
body = openapi_client.IoArgoprojArchivedworkflowV1alpha1Workflow() # IoArgoprojArchivedworkflowV1alpha1Workflow | The JSON schema of the Workflow to patch.

    try:
        api_response = api_instance.patch_namespaced_archivedworkflow(namespace, name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->patch_namespaced_archivedworkflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **name** | **str**| Unique Workflow name | 
 **body** | **IoArgoprojArchivedworkflowV1alpha1Workflow**| The JSON schema of the Workflow to patch. | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_cronworkflow**
> object patch_namespaced_cronworkflow(namespace, name, body)



patch the specified namespace scoped Workflow.

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The custom resource's namespace
name = 'name_example' # str | Unique Workflow name
body = openapi_client.IoArgoprojCronworkflowV1alpha1Workflow() # IoArgoprojCronworkflowV1alpha1Workflow | The JSON schema of the Workflow to patch.

    try:
        api_response = api_instance.patch_namespaced_cronworkflow(namespace, name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->patch_namespaced_cronworkflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **name** | **str**| Unique Workflow name | 
 **body** | **IoArgoprojCronworkflowV1alpha1Workflow**| The JSON schema of the Workflow to patch. | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_workflow**
> object patch_namespaced_workflow(namespace, name, body)



patch the specified namespace scoped Workflow.

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The custom resource's namespace
name = 'name_example' # str | Unique Workflow name
body = openapi_client.V1alpha1Workflow() # V1alpha1Workflow | The JSON schema of the Workflow to patch.

    try:
        api_response = api_instance.patch_namespaced_workflow(namespace, name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->patch_namespaced_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **name** | **str**| Unique Workflow name | 
 **body** | [**V1alpha1Workflow**](V1alpha1Workflow.md)| The JSON schema of the Workflow to patch. | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_workflowtemplate**
> V1alpha1WorkflowTemplate patch_namespaced_workflowtemplate(namespace, name, body)



patch the specified namespace scoped WorkflowTemplate.

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The custom resource's namespace
name = 'name_example' # str | Unique WorkflowTemplate name
body = openapi_client.V1alpha1WorkflowTemplate() # V1alpha1WorkflowTemplate | The JSON schema of the WorkflowTemplate to patch.

    try:
        api_response = api_instance.patch_namespaced_workflowtemplate(namespace, name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->patch_namespaced_workflowtemplate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **name** | **str**| Unique WorkflowTemplate name | 
 **body** | [**V1alpha1WorkflowTemplate**](V1alpha1WorkflowTemplate.md)| The JSON schema of the WorkflowTemplate to patch. | 

### Return type

[**V1alpha1WorkflowTemplate**](V1alpha1WorkflowTemplate.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_archivedworkflow**
> IoArgoprojArchivedworkflowV1alpha1Workflow replace_namespaced_archivedworkflow(namespace, name, body)



replace the specified namespace scoped Workflow.

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The custom resource's namespace
name = 'name_example' # str | Unique Workflow name
body = openapi_client.IoArgoprojArchivedworkflowV1alpha1Workflow() # IoArgoprojArchivedworkflowV1alpha1Workflow | The JSON schema of the Workflow to replace.

    try:
        api_response = api_instance.replace_namespaced_archivedworkflow(namespace, name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->replace_namespaced_archivedworkflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **name** | **str**| Unique Workflow name | 
 **body** | **IoArgoprojArchivedworkflowV1alpha1Workflow**| The JSON schema of the Workflow to replace. | 

### Return type

[**IoArgoprojArchivedworkflowV1alpha1Workflow**](IoArgoprojArchivedworkflowV1alpha1Workflow.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_cronworkflow**
> IoArgoprojCronworkflowV1alpha1Workflow replace_namespaced_cronworkflow(namespace, name, body)



replace the specified namespace scoped Workflow.

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The custom resource's namespace
name = 'name_example' # str | Unique Workflow name
body = openapi_client.IoArgoprojCronworkflowV1alpha1Workflow() # IoArgoprojCronworkflowV1alpha1Workflow | The JSON schema of the Workflow to replace.

    try:
        api_response = api_instance.replace_namespaced_cronworkflow(namespace, name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->replace_namespaced_cronworkflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **name** | **str**| Unique Workflow name | 
 **body** | **IoArgoprojCronworkflowV1alpha1Workflow**| The JSON schema of the Workflow to replace. | 

### Return type

[**IoArgoprojCronworkflowV1alpha1Workflow**](IoArgoprojCronworkflowV1alpha1Workflow.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_workflow**
> V1alpha1Workflow replace_namespaced_workflow(namespace, name, body)



replace the specified namespace scoped Workflow.

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The custom resource's namespace
name = 'name_example' # str | Unique Workflow name
body = openapi_client.V1alpha1Workflow() # V1alpha1Workflow | The JSON schema of the Workflow to replace.

    try:
        api_response = api_instance.replace_namespaced_workflow(namespace, name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->replace_namespaced_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **name** | **str**| Unique Workflow name | 
 **body** | [**V1alpha1Workflow**](V1alpha1Workflow.md)| The JSON schema of the Workflow to replace. | 

### Return type

[**V1alpha1Workflow**](V1alpha1Workflow.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_workflowtemplate**
> V1alpha1WorkflowTemplate replace_namespaced_workflowtemplate(namespace, name, body)



replace the specified namespace scoped WorkflowTemplate.

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.V1alpha1Api(api_client)
    namespace = 'namespace_example' # str | The custom resource's namespace
name = 'name_example' # str | Unique WorkflowTemplate name
body = openapi_client.V1alpha1WorkflowTemplate() # V1alpha1WorkflowTemplate | The JSON schema of the WorkflowTemplate to replace.

    try:
        api_response = api_instance.replace_namespaced_workflowtemplate(namespace, name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1alpha1Api->replace_namespaced_workflowtemplate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **name** | **str**| Unique WorkflowTemplate name | 
 **body** | [**V1alpha1WorkflowTemplate**](V1alpha1WorkflowTemplate.md)| The JSON schema of the WorkflowTemplate to replace. | 

### Return type

[**V1alpha1WorkflowTemplate**](V1alpha1WorkflowTemplate.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

