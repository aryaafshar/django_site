import datetime
import os
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
import torch
from skimage import io
import matplotlib.pyplot as plt
#Connect to the blob
account_name='mystorageaccount420245'

account_key='Qm4N7zcU//00AeeaE9FW1Drfveqxbt8btRsMBKGMsKaR4ab0u2pgGp6ugUqtX02TEk7WFoLzkrwa+AStaD0UJw=='
storage_connection_string='BlobEndpoint=https://mystorageaccount420245.blob.core.windows.net/;QueueEndpoint=https://mystorageaccount420245.queue.core.windows.net/;FileEndpoint=https://mystorageaccount420245.file.core.windows.net/;TableEndpoint=https://mystorageaccount420245.table.core.windows.net/;SharedAccessSignature=sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2023-11-11T13:04:05Z&st=2023-10-19T05:04:05Z&spr=https,http&sig=E9SSvsUCyweXgoZCm4%2BKX60V%2BMcM4E1o5%2F%2F%2BB6xzUyU%3D'
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
sas_url='https://'+'mystorageaccount420245'+'.blob.core.windows.net'+'/'+container_name+'/'+bloblist[1]+'?'+saslist[1]

#https://mystorageaccount420245.blob.core.windows.net/afsharfolder12/best.pt
#model=torch.hub.load_state_dict_from_url(sas_url)
#print(model.items())
# create a file-like object from the url
image=io.imread(sas_url)

# read the image file in a numpy array

plt.imshow(image)
plt.show()
print(sas_url)