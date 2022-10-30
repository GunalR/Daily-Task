import boto3
import glob
import os

service = boto3.client('s3')
folder_file=glob.glob('GunalR/*')
print(folder_file)
for file_name in folder_file:
     print(file_name)
     print(type(file_name))

     ff=(os.path.basename(file_name))


     print('Filename:',ff)

     print(type(file_name))
     response = service.upload_file(file_name, 'athiva-training','Gunal/'+ ff)
     print(response)