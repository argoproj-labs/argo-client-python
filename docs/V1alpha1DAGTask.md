# V1alpha1DAGTask

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | [**V1alpha1Arguments**](V1alpha1Arguments.md) | Arguments are the parameter and artifact arguments to the template | [optional] 
**continue_on** | [**V1alpha1ContinueOn**](V1alpha1ContinueOn.md) | ContinueOn makes argo to proceed with the following step even if this step fails. Errors and Failed states can be specified | [optional] 
**dependencies** | **list[str]** | Dependencies are name of other targets which this depends on | [optional] 
**name** | **str** | Name is the name of the target | 
**template** | **str** | Name of template to execute | 
**when** | **str** | When is an expression in which the task should conditionally execute | [optional] 
**with_items** | **list[str]** | WithItems expands a task into multiple parallel tasks from the items in the list | [optional] 
**with_param** | **str** | WithParam expands a task into multiple parallel tasks from the value in the parameter, which is expected to be a JSON list. | [optional] 
**with_sequence** | [**V1alpha1Sequence**](V1alpha1Sequence.md) | WithSequence expands a task into a numeric sequence | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


