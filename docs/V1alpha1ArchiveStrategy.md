# V1alpha1ArchiveStrategy

ArchiveStrategy describes how to archive files/directory when saving artifacts
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_none** | [**object**](.md) | NoneStrategy indicates to skip tar process and upload the files or directory tree as independent files. Note that if the artifact is a directory, the artifact driver must support the ability to save/load the directory appropriately. | [optional] 
**tar** | [**object**](.md) | TarStrategy will tar and gzip the file or directory when saving | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


