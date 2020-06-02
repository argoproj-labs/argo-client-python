# V1alpha1WorkflowSpec

WorkflowSpec is the specification of a Workflow.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_deadline_seconds** | **int** | Optional duration in seconds relative to the workflow start time which the workflow is allowed to run before the controller terminates the io.argoproj.workflow.v1alpha1. A value of zero is used to terminate a Running workflow | [optional] 
**affinity** | [**IoK8sApiCoreV1Affinity**](IoK8sApiCoreV1Affinity.md) |  | [optional] 
**arguments** | [**V1alpha1Arguments**](V1alpha1Arguments.md) |  | [optional] 
**artifact_repository_ref** | [**V1alpha1ArtifactRepositoryRef**](V1alpha1ArtifactRepositoryRef.md) |  | [optional] 
**automount_service_account_token** | **bool** | AutomountServiceAccountToken indicates whether a service account token should be automatically mounted in pods. ServiceAccountName of ExecutorConfig must be specified if this value is false. | [optional] 
**dns_config** | [**IoK8sApiCoreV1PodDNSConfig**](IoK8sApiCoreV1PodDNSConfig.md) |  | [optional] 
**dns_policy** | **str** | Set DNS policy for the pod. Defaults to \&quot;ClusterFirst\&quot;. Valid values are &#39;ClusterFirstWithHostNet&#39;, &#39;ClusterFirst&#39;, &#39;Default&#39; or &#39;None&#39;. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to &#39;ClusterFirstWithHostNet&#39;. | [optional] 
**entrypoint** | **str** | Entrypoint is a template reference to the starting point of the io.argoproj.workflow.v1alpha1. | [optional] 
**executor** | [**V1alpha1ExecutorConfig**](V1alpha1ExecutorConfig.md) |  | [optional] 
**host_aliases** | [**list[IoK8sApiCoreV1HostAlias]**](IoK8sApiCoreV1HostAlias.md) |  | [optional] 
**host_network** | **bool** | Host networking requested for this workflow pod. Default to false. | [optional] 
**image_pull_secrets** | [**list[IoK8sApiCoreV1LocalObjectReference]**](IoK8sApiCoreV1LocalObjectReference.md) | ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod | [optional] 
**metrics** | [**V1alpha1Metrics**](V1alpha1Metrics.md) |  | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector which will result in all pods of the workflow to be scheduled on the selected node(s). This is able to be overridden by a nodeSelector specified in the template. | [optional] 
**on_exit** | **str** | OnExit is a template reference which is invoked at the end of the workflow, irrespective of the success, failure, or error of the primary io.argoproj.workflow.v1alpha1. | [optional] 
**parallelism** | **int** | Parallelism limits the max total parallel pods that can execute at the same time in a workflow | [optional] 
**pod_disruption_budget** | [**IoK8sApiPolicyV1beta1PodDisruptionBudgetSpec**](IoK8sApiPolicyV1beta1PodDisruptionBudgetSpec.md) |  | [optional] 
**pod_gc** | [**V1alpha1PodGC**](V1alpha1PodGC.md) |  | [optional] 
**pod_priority** | **int** | Priority to apply to workflow pods. | [optional] 
**pod_priority_class_name** | **str** | PriorityClassName to apply to workflow pods. | [optional] 
**pod_spec_patch** | **str** | PodSpecPatch holds strategic merge patch to apply against the pod spec. Allows parameterization of container fields which are not strings (e.g. resource limits). | [optional] 
**priority** | **int** | Priority is used if controller is configured to process limited number of workflows in parallel. Workflows with higher priority are processed first. | [optional] 
**scheduler_name** | **str** | Set scheduler name for all pods. Will be overridden if container/script template&#39;s scheduler name is set. Default scheduler will be used if neither specified. | [optional] 
**security_context** | [**IoK8sApiCoreV1PodSecurityContext**](IoK8sApiCoreV1PodSecurityContext.md) |  | [optional] 
**service_account_name** | **str** | ServiceAccountName is the name of the ServiceAccount to run all pods of the workflow as. | [optional] 
**shutdown** | **str** | Shutdown will shutdown the workflow according to its ShutdownStrategy | [optional] 
**suspend** | **bool** | Suspend will suspend the workflow and prevent execution of any future steps in the workflow | [optional] 
**templates** | [**list[V1alpha1Template]**](V1alpha1Template.md) | Templates is a list of workflow templates used in a workflow | 
**tolerations** | [**list[IoK8sApiCoreV1Toleration]**](IoK8sApiCoreV1Toleration.md) | Tolerations to apply to workflow pods. | [optional] 
**ttl_seconds_after_finished** | **int** | TTLSecondsAfterFinished limits the lifetime of a Workflow that has finished execution (Succeeded, Failed, Error). If this field is set, once the Workflow finishes, it will be deleted after ttlSecondsAfterFinished expires. If this field is unset, ttlSecondsAfterFinished will not expire. If this field is set to zero, ttlSecondsAfterFinished expires immediately after the Workflow finishes. DEPRECATED: Use TTLStrategy.SecondsAfterCompletion instead. | [optional] 
**ttl_strategy** | [**V1alpha1TTLStrategy**](V1alpha1TTLStrategy.md) |  | [optional] 
**volume_claim_templates** | [**list[IoK8sApiCoreV1PersistentVolumeClaim]**](IoK8sApiCoreV1PersistentVolumeClaim.md) | VolumeClaimTemplates is a list of claims that containers are allowed to reference. The Workflow controller will create the claims at the beginning of the workflow and delete the claims upon completion of the workflow | [optional] 
**volumes** | [**list[IoK8sApiCoreV1Volume]**](IoK8sApiCoreV1Volume.md) | Volumes is a list of volumes that can be mounted by containers in a io.argoproj.workflow.v1alpha1. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


