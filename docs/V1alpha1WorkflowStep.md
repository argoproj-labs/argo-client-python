# V1alpha1WorkflowStep

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | [**V1alpha1Arguments**](V1alpha1Arguments.md) | Arguments hold arguments to the template | [optional] 
**continue_on** | [**V1alpha1ContinueOn**](V1alpha1ContinueOn.md) | ContinueOn makes argo to proceed with the following step even if this step fails. Errors and Failed states can be specified | [optional] 
**name** | **str** | Name of the step | [optional] 
**template** | **str** | Template is the name of the template to execute as the step | [optional] 
**template_ref** | [**V1alpha1TemplateRef**](V1alpha1TemplateRef.md) | TemplateRef is the reference to the template resource to execute as the step. | [optional] 
**when** | **str** | When is an expression in which the step should conditionally execute | [optional] 
**with_items** | **list[str]** | WithItems expands a step into multiple parallel steps from the items in the list | [optional] 
**with_param** | **str** | WithParam expands a step into multiple parallel steps from the value in the parameter, which is expected to be a JSON list. | [optional] 
**with_sequence** | [**V1alpha1Sequence**](V1alpha1Sequence.md) | WithSequence expands a step into a numeric sequence | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


