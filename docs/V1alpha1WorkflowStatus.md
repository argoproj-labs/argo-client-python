# V1alpha1WorkflowStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compressed_nodes** | **str** | Compressed and base64 decoded Nodes map | [optional] 
**finished_at** | **datetime** | Time at which this workflow completed | [optional] 
**message** | **str** | A human readable message indicating details about why the workflow is in this condition. | [optional] 
**nodes** | [**dict(str, V1alpha1NodeStatus)**](V1alpha1NodeStatus.md) | Nodes is a mapping between a node ID and the node&#39;s status. | [optional] 
**outputs** | [**V1alpha1Outputs**](V1alpha1Outputs.md) | Outputs captures output values and artifact locations produced by the workflow via global outputs | [optional] 
**persistent_volume_claims** | [**list[IoK8sApiCoreV1Volume]**](IoK8sApiCoreV1Volume.md) | PersistentVolumeClaims tracks all PVCs that were created as part of the workflow. The contents of this list are drained at the end of the workflow. | [optional] 
**phase** | **str** | Phase a simple, high-level summary of where the workflow is in its lifecycle. | [optional] 
**started_at** | **datetime** | Time at which this workflow started | [optional] 
**stored_templates** | [**dict(str, V1alpha1Template)**](V1alpha1Template.md) | StoredTemplates is a mapping between a template ref and the node&#39;s status. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


