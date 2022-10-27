import boto3
import os
import glob


service=boto3.client('s3')

folder_file=glob.glob('GunalR/*')
file=folder_file[0]
print(file)
filename=(os.path.basename(file))
print(filename)
#print(type(filename))
index=0
for files in range(1,5000):
    #print(files)
    index=index+1
    #obj=filename
    obj1=str(index)
    #print(obj1)
    obj= obj1 + filename

    #print(type(obj))
    print(obj)

    response=service.upload_file(file,'athiva-training', 'Gunal_5000/' + obj)
    print(response)