import datetime
import os
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
import torch

#Connect to the blob
account_name='mystorageaccount420245'

account_key='Qm4N7zcU//00AeeaE9FW1Drfveqxbt8btRsMBKGMsKaR4ab0u2pgGp6ugUqtX02TEk7WFoLzkrwa+AStaD0UJw=='
storage_connection_string='DefaultEndpointsProtocol=https;AccountName=mystorageaccount420245;AccountKey=Qm4N7zcU//00AeeaE9FW1Drfveqxbt8btRsMBKGMsKaR4ab0u2pgGp6ugUqtX02TEk7WFoLzkrwa+AStaD0UJw==;EndpointSuffix=core.windows.net'
Blob_Service_Client=BlobServiceClient.from_connection_string(storage_connection_string)
container_name='afsharfolder12'


def create_container(container):
    container_client=Blob_Service_Client.create_container(container)
    return container_client



#Upload my files
def upload_flies(folder):
     for file_name in os.listdir(folder):
      blob_obj=Blob_Service_Client.get_blob_client(container=container_name,blob=file_name)
      print(f'Uploading file: {file_name}...')
      with open(os.path.join(folder,file_name),mode='rb') as file_data:
        blob_obj.upload_blob(file_data)
def download_files(container):
   container_client=Blob_Service_Client.get_container_client(container)
          
blob_list=[]
sas_list=[]
def listMyblob(container,blist,sas):
  container_client=Blob_Service_Client.get_container_client(container)
  for b in container_client.list_blobs():
    blist.append(b.name)
    print(b.name)
  for blob in blist:
      sas_i=generate_blob_sas(account_name=account_name,container_name=container_name,blob_name=blob,account_key=account_key,permission=BlobSasPermissions(read=True))
      sas.append(sas_i)
  return sas,blist
saslist,bloblist=listMyblob(container=container_name,blist=blob_list,sas=sas_list)
sas_url='https://'+'mystorageaccount420245'+'.blob.core.windows.net'+'/'+container_name+'/'+bloblist[0]+'?'+saslist[0]

#https://mystorageaccount420245.blob.core.windows.net/afsharfolder12/best.pt
model=torch.hub.load_state_dict_from_url(sas_url)
print(model.items())
print(sas_url)