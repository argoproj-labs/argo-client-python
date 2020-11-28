# Argo Workflows Python Client

Python client for Argo Workflows

Argo Version: 2.11.8

## Installation

```bash
pip install argo-workflows
```

## Examples

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ArchivedWorkflowServiceApi* | [**deleteArchivedWorkflow**](docs/ArchivedWorkflowServiceApi.md#deleteArchivedWorkflow) | **DELETE** /api/v1/archived-workflows/{uid} |
*ArchivedWorkflowServiceApi* | [**getArchivedWorkflow**](docs/ArchivedWorkflowServiceApi.md#getArchivedWorkflow) | **GET** /api/v1/archived-workflows/{uid} |
*ArchivedWorkflowServiceApi* | [**listArchivedWorkflows**](docs/ArchivedWorkflowServiceApi.md#listArchivedWorkflows) | **GET** /api/v1/archived-workflows |
*ClusterWorkflowTemplateServiceApi* | [**createClusterWorkflowTemplate**](docs/ClusterWorkflowTemplateServiceApi.md#createClusterWorkflowTemplate) | **POST** /api/v1/cluster-workflow-templates |
*ClusterWorkflowTemplateServiceApi* | [**deleteClusterWorkflowTemplate**](docs/ClusterWorkflowTemplateServiceApi.md#deleteClusterWorkflowTemplate) | **DELETE** /api/v1/cluster-workflow-templates/{name} |
*ClusterWorkflowTemplateServiceApi* | [**getClusterWorkflowTemplate**](docs/ClusterWorkflowTemplateServiceApi.md#getClusterWorkflowTemplate) | **GET** /api/v1/cluster-workflow-templates/{name} |
*ClusterWorkflowTemplateServiceApi* | [**lintClusterWorkflowTemplate**](docs/ClusterWorkflowTemplateServiceApi.md#lintClusterWorkflowTemplate) | **POST** /api/v1/cluster-workflow-templates/lint |
*ClusterWorkflowTemplateServiceApi* | [**listClusterWorkflowTemplates**](docs/ClusterWorkflowTemplateServiceApi.md#listClusterWorkflowTemplates) | **GET** /api/v1/cluster-workflow-templates |
*ClusterWorkflowTemplateServiceApi* | [**updateClusterWorkflowTemplate**](docs/ClusterWorkflowTemplateServiceApi.md#updateClusterWorkflowTemplate) | **PUT** /api/v1/cluster-workflow-templates/{name} |
*CronWorkflowServiceApi* | [**createCronWorkflow**](docs/CronWorkflowServiceApi.md#createCronWorkflow) | **POST** /api/v1/cron-workflows/{namespace} |
*CronWorkflowServiceApi* | [**deleteCronWorkflow**](docs/CronWorkflowServiceApi.md#deleteCronWorkflow) | **DELETE** /api/v1/cron-workflows/{namespace}/{name} |
*CronWorkflowServiceApi* | [**getCronWorkflow**](docs/CronWorkflowServiceApi.md#getCronWorkflow) | **GET** /api/v1/cron-workflows/{namespace}/{name} |
*CronWorkflowServiceApi* | [**lintCronWorkflow**](docs/CronWorkflowServiceApi.md#lintCronWorkflow) | **POST** /api/v1/cron-workflows/{namespace}/lint |
*CronWorkflowServiceApi* | [**listCronWorkflows**](docs/CronWorkflowServiceApi.md#listCronWorkflows) | **GET** /api/v1/cron-workflows/{namespace} |
*CronWorkflowServiceApi* | [**updateCronWorkflow**](docs/CronWorkflowServiceApi.md#updateCronWorkflow) | **PUT** /api/v1/cron-workflows/{namespace}/{name} |
*EventServiceApi* | [**receiveEvent**](docs/EventServiceApi.md#receiveEvent) | **POST** /api/v1/events/{namespace}/{discriminator} |
*InfoServiceApi* | [**getInfo**](docs/InfoServiceApi.md#getInfo) | **GET** /api/v1/info |
*InfoServiceApi* | [**getUserInfo**](docs/InfoServiceApi.md#getUserInfo) | **GET** /api/v1/userinfo |
*InfoServiceApi* | [**getVersion**](docs/InfoServiceApi.md#getVersion) | **GET** /api/v1/version |
*WorkflowServiceApi* | [**createWorkflow**](docs/WorkflowServiceApi.md#createWorkflow) | **POST** /api/v1/workflows/{namespace} |
*WorkflowServiceApi* | [**deleteWorkflow**](docs/WorkflowServiceApi.md#deleteWorkflow) | **DELETE** /api/v1/workflows/{namespace}/{name} |
*WorkflowServiceApi* | [**getWorkflow**](docs/WorkflowServiceApi.md#getWorkflow) | **GET** /api/v1/workflows/{namespace}/{name} |
*WorkflowServiceApi* | [**lintWorkflow**](docs/WorkflowServiceApi.md#lintWorkflow) | **POST** /api/v1/workflows/{namespace}/lint |
*WorkflowServiceApi* | [**listWorkflows**](docs/WorkflowServiceApi.md#listWorkflows) | **GET** /api/v1/workflows/{namespace} |
*WorkflowServiceApi* | [**podLogs**](docs/WorkflowServiceApi.md#podLogs) | **GET** /api/v1/workflows/{namespace}/{name}/{podName}/log |
*WorkflowServiceApi* | [**resubmitWorkflow**](docs/WorkflowServiceApi.md#resubmitWorkflow) | **PUT** /api/v1/workflows/{namespace}/{name}/resubmit |
*WorkflowServiceApi* | [**resumeWorkflow**](docs/WorkflowServiceApi.md#resumeWorkflow) | **PUT** /api/v1/workflows/{namespace}/{name}/resume |
*WorkflowServiceApi* | [**retryWorkflow**](docs/WorkflowServiceApi.md#retryWorkflow) | **PUT** /api/v1/workflows/{namespace}/{name}/retry |
*WorkflowServiceApi* | [**setWorkflow**](docs/WorkflowServiceApi.md#setWorkflow) | **PUT** /api/v1/workflows/{namespace}/{name}/set |
*WorkflowServiceApi* | [**stopWorkflow**](docs/WorkflowServiceApi.md#stopWorkflow) | **PUT** /api/v1/workflows/{namespace}/{name}/stop |
*WorkflowServiceApi* | [**submitWorkflow**](docs/WorkflowServiceApi.md#submitWorkflow) | **POST** /api/v1/workflows/{namespace}/submit |
*WorkflowServiceApi* | [**suspendWorkflow**](docs/WorkflowServiceApi.md#suspendWorkflow) | **PUT** /api/v1/workflows/{namespace}/{name}/suspend |
*WorkflowServiceApi* | [**terminateWorkflow**](docs/WorkflowServiceApi.md#terminateWorkflow) | **PUT** /api/v1/workflows/{namespace}/{name}/terminate |
*WorkflowServiceApi* | [**watchEvents**](docs/WorkflowServiceApi.md#watchEvents) | **GET** /api/v1/stream/events/{namespace} |
*WorkflowServiceApi* | [**watchWorkflows**](docs/WorkflowServiceApi.md#watchWorkflows) | **GET** /api/v1/workflow-events/{namespace} |
*WorkflowTemplateServiceApi* | [**createWorkflowTemplate**](docs/WorkflowTemplateServiceApi.md#createWorkflowTemplate) | **POST** /api/v1/workflow-templates/{namespace} |
*WorkflowTemplateServiceApi* | [**deleteWorkflowTemplate**](docs/WorkflowTemplateServiceApi.md#deleteWorkflowTemplate) | **DELETE** /api/v1/workflow-templates/{namespace}/{name} |
*WorkflowTemplateServiceApi* | [**getWorkflowTemplate**](docs/WorkflowTemplateServiceApi.md#getWorkflowTemplate) | **GET** /api/v1/workflow-templates/{namespace}/{name} |
*WorkflowTemplateServiceApi* | [**lintWorkflowTemplate**](docs/WorkflowTemplateServiceApi.md#lintWorkflowTemplate) | **POST** /api/v1/workflow-templates/{namespace}/lint |
*WorkflowTemplateServiceApi* | [**listWorkflowTemplates**](docs/WorkflowTemplateServiceApi.md#listWorkflowTemplates) | **GET** /api/v1/workflow-templates/{namespace} |
*WorkflowTemplateServiceApi* | [**updateWorkflowTemplate**](docs/WorkflowTemplateServiceApi.md#updateWorkflowTemplate) | **PUT** /api/v1/workflow-templates/{namespace}/{name} |


## Documentation for Models

 - [AWSElasticBlockStoreVolumeSource](docs/AWSElasticBlockStoreVolumeSource.md)
 - [ArchiveStrategy](docs/ArchiveStrategy.md)
 - [Arguments](docs/Arguments.md)
 - [Artifact](docs/Artifact.md)
 - [ArtifactLocation](docs/ArtifactLocation.md)
 - [ArtifactRepositoryRef](docs/ArtifactRepositoryRef.md)
 - [ArtifactoryArtifact](docs/ArtifactoryArtifact.md)
 - [AzureDiskVolumeSource](docs/AzureDiskVolumeSource.md)
 - [AzureFileVolumeSource](docs/AzureFileVolumeSource.md)
 - [Backoff](docs/Backoff.md)
 - [CSIVolumeSource](docs/CSIVolumeSource.md)
 - [Cache](docs/Cache.md)
 - [Capabilities](docs/Capabilities.md)
 - [CephFSVolumeSource](docs/CephFSVolumeSource.md)
 - [CinderVolumeSource](docs/CinderVolumeSource.md)
 - [ClusterWorkflowTemplate](docs/ClusterWorkflowTemplate.md)
 - [ClusterWorkflowTemplateCreateRequest](docs/ClusterWorkflowTemplateCreateRequest.md)
 - [ClusterWorkflowTemplateLintRequest](docs/ClusterWorkflowTemplateLintRequest.md)
 - [ClusterWorkflowTemplateList](docs/ClusterWorkflowTemplateList.md)
 - [ClusterWorkflowTemplateUpdateRequest](docs/ClusterWorkflowTemplateUpdateRequest.md)
 - [Condition](docs/Condition.md)
 - [ConfigMapEnvSource](docs/ConfigMapEnvSource.md)
 - [ConfigMapProjection](docs/ConfigMapProjection.md)
 - [ConfigMapVolumeSource](docs/ConfigMapVolumeSource.md)
 - [ContinueOn](docs/ContinueOn.md)
 - [Counter](docs/Counter.md)
 - [CreateCronWorkflowRequest](docs/CreateCronWorkflowRequest.md)
 - [CreateOptions](docs/CreateOptions.md)
 - [CronWorkflow](docs/CronWorkflow.md)
 - [CronWorkflowList](docs/CronWorkflowList.md)
 - [CronWorkflowSpec](docs/CronWorkflowSpec.md)
 - [CronWorkflowStatus](docs/CronWorkflowStatus.md)
 - [DAGTask](docs/DAGTask.md)
 - [DAGTemplate](docs/DAGTemplate.md)
 - [DownwardAPIProjection](docs/DownwardAPIProjection.md)
 - [DownwardAPIVolumeFile](docs/DownwardAPIVolumeFile.md)
 - [DownwardAPIVolumeSource](docs/DownwardAPIVolumeSource.md)
 - [EmptyDirVolumeSource](docs/EmptyDirVolumeSource.md)
 - [EnvVarSource](docs/EnvVarSource.md)
 - [Event](docs/Event.md)
 - [EventSeries](docs/EventSeries.md)
 - [EventSource](docs/EventSource.md)
 - [ExecAction](docs/ExecAction.md)
 - [ExecutorConfig](docs/ExecutorConfig.md)
 - [FCVolumeSource](docs/FCVolumeSource.md)
 - [FlexVolumeSource](docs/FlexVolumeSource.md)
 - [FlockerVolumeSource](docs/FlockerVolumeSource.md)
 - [GCEPersistentDiskVolumeSource](docs/GCEPersistentDiskVolumeSource.md)
 - [GCSArtifact](docs/GCSArtifact.md)
 - [Gauge](docs/Gauge.md)
 - [GetUserInfoResponse](docs/GetUserInfoResponse.md)
 - [GitArtifact](docs/GitArtifact.md)
 - [GitRepoVolumeSource](docs/GitRepoVolumeSource.md)
 - [GlusterfsVolumeSource](docs/GlusterfsVolumeSource.md)
 - [GoogleProtobufAny](docs/GoogleProtobufAny.md)
 - [GrpcGatewayRuntimeStreamError](docs/GrpcGatewayRuntimeStreamError.md)
 - [HDFSArtifact](docs/HDFSArtifact.md)
 - [HTTPArtifact](docs/HTTPArtifact.md)
 - [HTTPGetAction](docs/HTTPGetAction.md)
 - [HTTPHeader](docs/HTTPHeader.md)
 - [Handler](docs/Handler.md)
 - [Histogram](docs/Histogram.md)
 - [HostPathVolumeSource](docs/HostPathVolumeSource.md)
 - [ISCSIVolumeSource](docs/ISCSIVolumeSource.md)
 - [InfoResponse](docs/InfoResponse.md)
 - [Initializer](docs/Initializer.md)
 - [Initializers](docs/Initializers.md)
 - [Inputs](docs/Inputs.md)
 - [IoK8sApiPolicyV1beta1PodDisruptionBudgetSpec](docs/IoK8sApiPolicyV1beta1PodDisruptionBudgetSpec.md)
 - [KeyToPath](docs/KeyToPath.md)
 - [LabelSelector](docs/LabelSelector.md)
 - [LabelSelectorRequirement](docs/LabelSelectorRequirement.md)
 - [Link](docs/Link.md)
 - [LintCronWorkflowRequest](docs/LintCronWorkflowRequest.md)
 - [LogEntry](docs/LogEntry.md)
 - [ManagedFieldsEntry](docs/ManagedFieldsEntry.md)
 - [MemoizationStatus](docs/MemoizationStatus.md)
 - [Memoize](docs/Memoize.md)
 - [Metadata](docs/Metadata.md)
 - [MetricLabel](docs/MetricLabel.md)
 - [Metrics](docs/Metrics.md)
 - [Mutex](docs/Mutex.md)
 - [MutexHolding](docs/MutexHolding.md)
 - [MutexStatus](docs/MutexStatus.md)
 - [NFSVolumeSource](docs/NFSVolumeSource.md)
 - [NodeAffinity](docs/NodeAffinity.md)
 - [NodeSelector](docs/NodeSelector.md)
 - [NodeSelectorRequirement](docs/NodeSelectorRequirement.md)
 - [NodeSelectorTerm](docs/NodeSelectorTerm.md)
 - [NodeStatus](docs/NodeStatus.md)
 - [NodeSynchronizationStatus](docs/NodeSynchronizationStatus.md)
 - [OSSArtifact](docs/OSSArtifact.md)
 - [ObjectFieldSelector](docs/ObjectFieldSelector.md)
 - [Outputs](docs/Outputs.md)
 - [OwnerReference](docs/OwnerReference.md)
 - [ParallelSteps](docs/ParallelSteps.md)
 - [Parameter](docs/Parameter.md)
 - [PersistentVolumeClaimCondition](docs/PersistentVolumeClaimCondition.md)
 - [PersistentVolumeClaimSpec](docs/PersistentVolumeClaimSpec.md)
 - [PersistentVolumeClaimStatus](docs/PersistentVolumeClaimStatus.md)
 - [PersistentVolumeClaimVolumeSource](docs/PersistentVolumeClaimVolumeSource.md)
 - [PhotonPersistentDiskVolumeSource](docs/PhotonPersistentDiskVolumeSource.md)
 - [PodAffinity](docs/PodAffinity.md)
 - [PodAffinityTerm](docs/PodAffinityTerm.md)
 - [PodAntiAffinity](docs/PodAntiAffinity.md)
 - [PodDNSConfigOption](docs/PodDNSConfigOption.md)
 - [PodGC](docs/PodGC.md)
 - [PortworxVolumeSource](docs/PortworxVolumeSource.md)
 - [PreferredSchedulingTerm](docs/PreferredSchedulingTerm.md)
 - [ProjectedVolumeSource](docs/ProjectedVolumeSource.md)
 - [Prometheus](docs/Prometheus.md)
 - [QuobyteVolumeSource](docs/QuobyteVolumeSource.md)
 - [RBDVolumeSource](docs/RBDVolumeSource.md)
 - [RawArtifact](docs/RawArtifact.md)
 - [ResourceFieldSelector](docs/ResourceFieldSelector.md)
 - [ResourceTemplate](docs/ResourceTemplate.md)
 - [RetryStrategy](docs/RetryStrategy.md)
 - [S3Artifact](docs/S3Artifact.md)
 - [SELinuxOptions](docs/SELinuxOptions.md)
 - [ScaleIOVolumeSource](docs/ScaleIOVolumeSource.md)
 - [ScriptTemplate](docs/ScriptTemplate.md)
 - [SecretEnvSource](docs/SecretEnvSource.md)
 - [SecretProjection](docs/SecretProjection.md)
 - [SecretVolumeSource](docs/SecretVolumeSource.md)
 - [SemaphoreHolding](docs/SemaphoreHolding.md)
 - [SemaphoreRef](docs/SemaphoreRef.md)
 - [SemaphoreStatus](docs/SemaphoreStatus.md)
 - [Sequence](docs/Sequence.md)
 - [ServiceAccountTokenProjection](docs/ServiceAccountTokenProjection.md)
 - [Status](docs/Status.md)
 - [StatusCause](docs/StatusCause.md)
 - [StatusDetails](docs/StatusDetails.md)
 - [StorageOSVolumeSource](docs/StorageOSVolumeSource.md)
 - [StreamResultOfEvent](docs/StreamResultOfEvent.md)
 - [StreamResultOfLogEntry](docs/StreamResultOfLogEntry.md)
 - [StreamResultOfWorkflowWatchEvent](docs/StreamResultOfWorkflowWatchEvent.md)
 - [Submit](docs/Submit.md)
 - [SubmitOpts](docs/SubmitOpts.md)
 - [SuspendTemplate](docs/SuspendTemplate.md)
 - [Synchronization](docs/Synchronization.md)
 - [SynchronizationStatus](docs/SynchronizationStatus.md)
 - [Sysctl](docs/Sysctl.md)
 - [TCPSocketAction](docs/TCPSocketAction.md)
 - [TTLStrategy](docs/TTLStrategy.md)
 - [TarStrategy](docs/TarStrategy.md)
 - [Template](docs/Template.md)
 - [TemplateRef](docs/TemplateRef.md)
 - [TypedLocalObjectReference](docs/TypedLocalObjectReference.md)
 - [UpdateCronWorkflowRequest](docs/UpdateCronWorkflowRequest.md)
 - [UserContainer](docs/UserContainer.md)
 - [ValueFrom](docs/ValueFrom.md)
 - [Version](docs/Version.md)
 - [VolumeProjection](docs/VolumeProjection.md)
 - [VsphereVirtualDiskVolumeSource](docs/VsphereVirtualDiskVolumeSource.md)
 - [WeightedPodAffinityTerm](docs/WeightedPodAffinityTerm.md)
 - [WindowsSecurityContextOptions](docs/WindowsSecurityContextOptions.md)
 - [Workflow](docs/Workflow.md)
 - [WorkflowCreateRequest](docs/WorkflowCreateRequest.md)
 - [WorkflowEventBinding](docs/WorkflowEventBinding.md)
 - [WorkflowEventBindingSpec](docs/WorkflowEventBindingSpec.md)
 - [WorkflowLintRequest](docs/WorkflowLintRequest.md)
 - [WorkflowList](docs/WorkflowList.md)
 - [WorkflowResubmitRequest](docs/WorkflowResubmitRequest.md)
 - [WorkflowResumeRequest](docs/WorkflowResumeRequest.md)
 - [WorkflowRetryRequest](docs/WorkflowRetryRequest.md)
 - [WorkflowSetRequest](docs/WorkflowSetRequest.md)
 - [WorkflowSpec](docs/WorkflowSpec.md)
 - [WorkflowStatus](docs/WorkflowStatus.md)
 - [WorkflowStep](docs/WorkflowStep.md)
 - [WorkflowStopRequest](docs/WorkflowStopRequest.md)
 - [WorkflowSubmitRequest](docs/WorkflowSubmitRequest.md)
 - [WorkflowSuspendRequest](docs/WorkflowSuspendRequest.md)
 - [WorkflowTemplate](docs/WorkflowTemplate.md)
 - [WorkflowTemplateCreateRequest](docs/WorkflowTemplateCreateRequest.md)
 - [WorkflowTemplateLintRequest](docs/WorkflowTemplateLintRequest.md)
 - [WorkflowTemplateList](docs/WorkflowTemplateList.md)
 - [WorkflowTemplateRef](docs/WorkflowTemplateRef.md)
 - [WorkflowTemplateSpec](docs/WorkflowTemplateSpec.md)
 - [WorkflowTemplateUpdateRequest](docs/WorkflowTemplateUpdateRequest.md)
 - [WorkflowTerminateRequest](docs/WorkflowTerminateRequest.md)
 - [WorkflowWatchEvent](docs/WorkflowWatchEvent.md)



## Code generation

The generated SDK will correspond to the argo version specified in the [ARGO_VERSION](./ARGO_VERSION) file.

If you wish to generate code yourself, you can do so by reproducing the build environment (image): `make builder_image`, then running `make builder_make` to generate the client.
