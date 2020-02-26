# workflows.client.InfoServiceApi

All URIs are relative to *http://localhost:2746*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_info**](InfoServiceApi.md#get_info) | **GET** /api/v1/info | 


# **get_info**
> V1alpha1InfoResponse get_info()



### Example
```python
from __future__ import print_function
import time
import workflows.client
from workflows.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = workflows.client.InfoServiceApi()

try:
    api_response = api_instance.get_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoServiceApi->get_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1alpha1InfoResponse**](V1alpha1InfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

