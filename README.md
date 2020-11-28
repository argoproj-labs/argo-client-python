# Argo Workflows Python Client

Python client for Argo Workflows

Argo Version: 2.11.8

## Installation

```bash
pip install argo-workflows
```

## Examples

A quick start example with one of the example workflow
```python
import yaml
import requests
from argo.workflows.client import (ApiClient,
                                   WorkflowServiceApi,
                                   Configuration,
                                   V1alpha1WorkflowCreateRequest)

# assume we ran `kubectl -n argo port-forward deployment/argo-server 2746:2746`

config = Configuration(host="http://localhost:2746")
client = ApiClient(configuration=config)
service = WorkflowServiceApi(api_client=client)
WORKFLOW = 'https://raw.githubusercontent.com/argoproj/argo/v2.11.8/examples/dag-diamond-steps.yaml'

resp = requests.get(WORKFLOW)
manifest: dict = yaml.safe_load(resp.text)

service.create_workflow('argo', V1alpha1WorkflowCreateRequest(workflow=manifest))
```

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
 - [V1AzureDiskVolumeSource](V1AzureDiskVolumeSource.md)
 - [V1alpha1Arguments](V1alpha1Arguments.md)
 - [V1alpha1CronWorkflowSpec](V1alpha1CronWorkflowSpec.md)
 - [V1alpha1WorkflowSetRequest](V1alpha1WorkflowSetRequest.md)
 - [V1ConfigMapProjection](V1ConfigMapProjection.md)
 - [V1Volume](V1Volume.md)
 - [V1alpha1WorkflowLintRequest](V1alpha1WorkflowLintRequest.md)
 - [V1alpha1MetricLabel](V1alpha1MetricLabel.md)
 - [V1PortworxVolumeSource](V1PortworxVolumeSource.md)
 - [V1alpha1Histogram](V1alpha1Histogram.md)
 - [V1alpha1ArtifactoryArtifact](V1alpha1ArtifactoryArtifact.md)
 - [V1alpha1ClusterWorkflowTemplateCreateRequest](V1alpha1ClusterWorkflowTemplateCreateRequest.md)
 - [V1EnvVar](V1EnvVar.md)
 - [V1SecretKeySelector](V1SecretKeySelector.md)
 - [V1StorageOSVolumeSource](V1StorageOSVolumeSource.md)
 - [V1StatusDetails](V1StatusDetails.md)
 - [V1ObjectMeta](V1ObjectMeta.md)
 - [V1alpha1WorkflowResubmitRequest](V1alpha1WorkflowResubmitRequest.md)
 - [V1alpha1ContinueOn](V1alpha1ContinueOn.md)
 - [V1alpha1Sequence](V1alpha1Sequence.md)
 - [V1alpha1WorkflowResumeRequest](V1alpha1WorkflowResumeRequest.md)
 - [V1PodAffinityTerm](V1PodAffinityTerm.md)
 - [V1alpha1ValueFrom](V1alpha1ValueFrom.md)
 - [V1ServiceAccountTokenProjection](V1ServiceAccountTokenProjection.md)
 - [V1TypedLocalObjectReference](V1TypedLocalObjectReference.md)
 - [V1alpha1LogEntry](V1alpha1LogEntry.md)
 - [V1ISCSIVolumeSource](V1ISCSIVolumeSource.md)
 - [V1EventSeries](V1EventSeries.md)
 - [V1alpha1WorkflowTemplate](V1alpha1WorkflowTemplate.md)
 - [V1TCPSocketAction](V1TCPSocketAction.md)
 - [V1Initializer](V1Initializer.md)
 - [V1NodeSelectorRequirement](V1NodeSelectorRequirement.md)
 - [V1CreateOptions](V1CreateOptions.md)
 - [V1ConfigMapEnvSource](V1ConfigMapEnvSource.md)
 - [V1VolumeDevice](V1VolumeDevice.md)
 - [V1VolumeProjection](V1VolumeProjection.md)
 - [V1DownwardAPIVolumeFile](V1DownwardAPIVolumeFile.md)
 - [V1alpha1WorkflowStep](V1alpha1WorkflowStep.md)
 - [V1PodDNSConfigOption](V1PodDNSConfigOption.md)
 - [V1PodDNSConfig](V1PodDNSConfig.md)
 - [V1alpha1UserContainer](V1alpha1UserContainer.md)
 - [V1StatusCause](V1StatusCause.md)
 - [V1Capabilities](V1Capabilities.md)
 - [V1RBDVolumeSource](V1RBDVolumeSource.md)
 - [V1HTTPGetAction](V1HTTPGetAction.md)
 - [V1OwnerReference](V1OwnerReference.md)
 - [V1alpha1ResourceTemplate](V1alpha1ResourceTemplate.md)
 - [V1Initializers](V1Initializers.md)
 - [V1alpha1WorkflowTemplateList](V1alpha1WorkflowTemplateList.md)
 - [V1alpha1Inputs](V1alpha1Inputs.md)
 - [V1alpha1DAGTemplate](V1alpha1DAGTemplate.md)
 - [V1ExecAction](V1ExecAction.md)
 - [V1alpha1CronWorkflowList](V1alpha1CronWorkflowList.md)
 - [V1alpha1WorkflowCreateRequest](V1alpha1WorkflowCreateRequest.md)
 - [V1alpha1HDFSArtifact](V1alpha1HDFSArtifact.md)
 - [V1KeyToPath](V1KeyToPath.md)
 - [V1Event](V1Event.md)
 - [V1alpha1ClusterWorkflowTemplateList](V1alpha1ClusterWorkflowTemplateList.md)
 - [V1SELinuxOptions](V1SELinuxOptions.md)
 - [V1HostPathVolumeSource](V1HostPathVolumeSource.md)
 - [V1Sysctl](V1Sysctl.md)
 - [V1ConfigMapKeySelector](V1ConfigMapKeySelector.md)
 - [V1EmptyDirVolumeSource](V1EmptyDirVolumeSource.md)
 - [V1GlusterfsVolumeSource](V1GlusterfsVolumeSource.md)
 - [V1ContainerPort](V1ContainerPort.md)
 - [V1AWSElasticBlockStoreVolumeSource](V1AWSElasticBlockStoreVolumeSource.md)
 - [V1PreferredSchedulingTerm](V1PreferredSchedulingTerm.md)
 - [V1ObjectReference](V1ObjectReference.md)
 - [V1alpha1ScriptTemplate](V1alpha1ScriptTemplate.md)
 - [V1PodAntiAffinity](V1PodAntiAffinity.md)
 - [V1NodeSelectorTerm](V1NodeSelectorTerm.md)
 - [V1EnvFromSource](V1EnvFromSource.md)
 - [V1LabelSelectorRequirement](V1LabelSelectorRequirement.md)
 - [V1ManagedFieldsEntry](V1ManagedFieldsEntry.md)
 - [V1alpha1WorkflowEventBindingSpec](V1alpha1WorkflowEventBindingSpec.md)
 - [V1alpha1MutexHolding](V1alpha1MutexHolding.md)
 - [V1alpha1S3Artifact](V1alpha1S3Artifact.md)
 - [V1ConfigMapVolumeSource](V1ConfigMapVolumeSource.md)
 - [V1alpha1CronWorkflow](V1alpha1CronWorkflow.md)
 - [V1alpha1SubmitOpts](V1alpha1SubmitOpts.md)
 - [V1PodAffinity](V1PodAffinity.md)
 - [V1alpha1Mutex](V1alpha1Mutex.md)
 - [V1Toleration](V1Toleration.md)
 - [V1alpha1Outputs](V1alpha1Outputs.md)
 - [V1CinderVolumeSource](V1CinderVolumeSource.md)
 - [V1SecretProjection](V1SecretProjection.md)
 - [V1SecurityContext](V1SecurityContext.md)
 - [V1alpha1WorkflowRetryRequest](V1alpha1WorkflowRetryRequest.md)
 - [V1GitRepoVolumeSource](V1GitRepoVolumeSource.md)
 - [V1alpha1Metadata](V1alpha1Metadata.md)
 - [V1Status](V1Status.md)
 - [V1alpha1NodeSynchronizationStatus](V1alpha1NodeSynchronizationStatus.md)
 - [V1ScaleIOVolumeSource](V1ScaleIOVolumeSource.md)
 - [V1PersistentVolumeClaim](V1PersistentVolumeClaim.md)
 - [V1alpha1Artifact](V1alpha1Artifact.md)
 - [V1alpha1NodeStatus](V1alpha1NodeStatus.md)
 - [V1FlexVolumeSource](V1FlexVolumeSource.md)
 - [V1alpha1OSSArtifact](V1alpha1OSSArtifact.md)
 - [V1alpha1WorkflowTemplateRef](V1alpha1WorkflowTemplateRef.md)
 - [V1WeightedPodAffinityTerm](V1WeightedPodAffinityTerm.md)
 - [V1alpha1ClusterWorkflowTemplateUpdateRequest](V1alpha1ClusterWorkflowTemplateUpdateRequest.md)
 - [V1alpha1Counter](V1alpha1Counter.md)
 - [V1alpha1SemaphoreRef](V1alpha1SemaphoreRef.md)
 - [V1alpha1ArchiveStrategy](V1alpha1ArchiveStrategy.md)
 - [V1alpha1WorkflowTemplateSpec](V1alpha1WorkflowTemplateSpec.md)
 - [V1EnvVarSource](V1EnvVarSource.md)
 - [V1alpha1Synchronization](V1alpha1Synchronization.md)
 - [V1alpha1Metrics](V1alpha1Metrics.md)
 - [V1AzureFileVolumeSource](V1AzureFileVolumeSource.md)
 - [V1alpha1Event](V1alpha1Event.md)
 - [V1alpha1Memoize](V1alpha1Memoize.md)
 - [V1alpha1ClusterWorkflowTemplateLintRequest](V1alpha1ClusterWorkflowTemplateLintRequest.md)
 - [V1alpha1WorkflowList](V1alpha1WorkflowList.md)
 - [V1alpha1Gauge](V1alpha1Gauge.md)
 - [V1alpha1SemaphoreStatus](V1alpha1SemaphoreStatus.md)
 - [V1GCEPersistentDiskVolumeSource](V1GCEPersistentDiskVolumeSource.md)
 - [V1alpha1RawArtifact](V1alpha1RawArtifact.md)
 - [V1alpha1ArtifactRepositoryRef](V1alpha1ArtifactRepositoryRef.md)
 - [V1ResourceFieldSelector](V1ResourceFieldSelector.md)
 - [V1PersistentVolumeClaimSpec](V1PersistentVolumeClaimSpec.md)
 - [V1alpha1Parameter](V1alpha1Parameter.md)
 - [V1PersistentVolumeClaimCondition](V1PersistentVolumeClaimCondition.md)
 - [V1Lifecycle](V1Lifecycle.md)
 - [V1alpha1PodGC](V1alpha1PodGC.md)
 - [V1alpha1LintCronWorkflowRequest](V1alpha1LintCronWorkflowRequest.md)
 - [V1DownwardAPIVolumeSource](V1DownwardAPIVolumeSource.md)
 - [V1alpha1Workflow](V1alpha1Workflow.md)
 - [V1VolumeMount](V1VolumeMount.md)
 - [V1EventSource](V1EventSource.md)
 - [V1LabelSelector](V1LabelSelector.md)
 - [V1VsphereVirtualDiskVolumeSource](V1VsphereVirtualDiskVolumeSource.md)
 - [V1alpha1TemplateRef](V1alpha1TemplateRef.md)
 - [V1alpha1CreateCronWorkflowRequest](V1alpha1CreateCronWorkflowRequest.md)
 - [V1alpha1GitArtifact](V1alpha1GitArtifact.md)
 - [V1ProjectedVolumeSource](V1ProjectedVolumeSource.md)
 - [V1SecretEnvSource](V1SecretEnvSource.md)
 - [V1PhotonPersistentDiskVolumeSource](V1PhotonPersistentDiskVolumeSource.md)
 - [V1alpha1WorkflowWatchEvent](V1alpha1WorkflowWatchEvent.md)
 - [V1alpha1DAGTask](V1alpha1DAGTask.md)
 - [V1alpha1CronWorkflowStatus](V1alpha1CronWorkflowStatus.md)
 - [V1alpha1WorkflowSuspendRequest](V1alpha1WorkflowSuspendRequest.md)
 - [V1CSIVolumeSource](V1CSIVolumeSource.md)
 - [V1alpha1Submit](V1alpha1Submit.md)
 - [V1alpha1GCSArtifact](V1alpha1GCSArtifact.md)
 - [V1alpha1HTTPArtifact](V1alpha1HTTPArtifact.md)
 - [V1alpha1Version](V1alpha1Version.md)
 - [V1Container](V1Container.md)
 - [V1alpha1ClusterWorkflowTemplate](V1alpha1ClusterWorkflowTemplate.md)
 - [V1alpha1WorkflowTemplateUpdateRequest](V1alpha1WorkflowTemplateUpdateRequest.md)
 - [V1FCVolumeSource](V1FCVolumeSource.md)
 - [V1Affinity](V1Affinity.md)
 - [V1alpha1SemaphoreHolding](V1alpha1SemaphoreHolding.md)
 - [V1alpha1TTLStrategy](V1alpha1TTLStrategy.md)
 - [V1alpha1WorkflowSubmitRequest](V1alpha1WorkflowSubmitRequest.md)
 - [V1Handler](V1Handler.md)
 - [V1HTTPHeader](V1HTTPHeader.md)
 - [V1ListMeta](V1ListMeta.md)
 - [V1alpha1SuspendTemplate](V1alpha1SuspendTemplate.md)
 - [V1alpha1WorkflowStatus](V1alpha1WorkflowStatus.md)
 - [V1alpha1WorkflowTemplateCreateRequest](V1alpha1WorkflowTemplateCreateRequest.md)
 - [V1PersistentVolumeClaimStatus](V1PersistentVolumeClaimStatus.md)
 - [V1alpha1Link](V1alpha1Link.md)
 - [V1alpha1WorkflowSpec](V1alpha1WorkflowSpec.md)
 - [V1PersistentVolumeClaimVolumeSource](V1PersistentVolumeClaimVolumeSource.md)
 - [V1ResourceRequirements](V1ResourceRequirements.md)
 - [V1FlockerVolumeSource](V1FlockerVolumeSource.md)
 - [V1NodeSelector](V1NodeSelector.md)
 - [V1alpha1ArtifactLocation](V1alpha1ArtifactLocation.md)
 - [V1alpha1InfoResponse](V1alpha1InfoResponse.md)
 - [V1alpha1TarStrategy](V1alpha1TarStrategy.md)
 - [V1alpha1WorkflowStopRequest](V1alpha1WorkflowStopRequest.md)
 - [V1ObjectFieldSelector](V1ObjectFieldSelector.md)
 - [V1NFSVolumeSource](V1NFSVolumeSource.md)
 - [V1alpha1Condition](V1alpha1Condition.md)
 - [V1CephFSVolumeSource](V1CephFSVolumeSource.md)
 - [V1alpha1ExecutorConfig](V1alpha1ExecutorConfig.md)
 - [V1alpha1Prometheus](V1alpha1Prometheus.md)
 - [V1alpha1GetUserInfoResponse](V1alpha1GetUserInfoResponse.md)
 - [V1alpha1Backoff](V1alpha1Backoff.md)
 - [V1alpha1WorkflowEventBinding](V1alpha1WorkflowEventBinding.md)
 - [V1alpha1Template](V1alpha1Template.md)
 - [V1QuobyteVolumeSource](V1QuobyteVolumeSource.md)
 - [V1PodSecurityContext](V1PodSecurityContext.md)
 - [V1WindowsSecurityContextOptions](V1WindowsSecurityContextOptions.md)
 - [V1LocalObjectReference](V1LocalObjectReference.md)
 - [V1NodeAffinity](V1NodeAffinity.md)
 - [V1HostAlias](V1HostAlias.md)
 - [V1alpha1MemoizationStatus](V1alpha1MemoizationStatus.md)
 - [V1alpha1SynchronizationStatus](V1alpha1SynchronizationStatus.md)
 - [V1alpha1UpdateCronWorkflowRequest](V1alpha1UpdateCronWorkflowRequest.md)
 - [V1SecretVolumeSource](V1SecretVolumeSource.md)
 - [V1Probe](V1Probe.md)
 - [V1alpha1Cache](V1alpha1Cache.md)
 - [V1alpha1RetryStrategy](V1alpha1RetryStrategy.md)
 - [V1alpha1WorkflowTemplateLintRequest](V1alpha1WorkflowTemplateLintRequest.md)
 - [V1alpha1WorkflowTerminateRequest](V1alpha1WorkflowTerminateRequest.md)
 - [V1alpha1MutexStatus](V1alpha1MutexStatus.md)
 - [V1DownwardAPIProjection](V1DownwardAPIProjection.md)


## Code generation

The generated SDK will correspond to the argo version specified in the [ARGO_VERSION](./ARGO_VERSION) file.

If you wish to generate code yourself, you can do so by reproducing the build environment (image): `make builder_image`, then running `make builder_make` to generate the client.
