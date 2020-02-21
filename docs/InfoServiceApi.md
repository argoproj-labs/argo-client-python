# workflows.client.InfoServiceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_info**](InfoServiceApi.md#get_info) | **GET** /api/v1/info | 


# **get_info**
> InfoInfoResponse get_info()



### Example
```python
from __future__ import print_function
import time
import workflows.client
from workflows.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = workflows.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = workflows.client.InfoServiceApi(workflows.client.ApiClient(configuration))

try:
    api_response = api_instance.get_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoServiceApi->get_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InfoInfoResponse**](InfoInfoResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

