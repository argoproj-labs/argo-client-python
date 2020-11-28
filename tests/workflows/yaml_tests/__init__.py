from argo.workflows.client import (WorkflowServiceApi,
                                   ApiClient,
                                   Configuration,
                                   V1alpha1WorkflowCreateRequest)




def create_workflow(ns, manifest):
    config = Configuration(host="http://localhost:2746")
    client = ApiClient(configuration=config)
    service = WorkflowServiceApi(api_client=client)
    service.create_workflow(ns, V1alpha1WorkflowCreateRequest(workflow=manifest))
