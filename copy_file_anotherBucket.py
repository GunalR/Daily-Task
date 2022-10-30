import boto3
services=boto3.client('s3')


response=services.list_objects(Bucket='athiva-training')
#print(type(response))
#print(response)

for file in (response['Contents']):
    #print(file['Key'])

    destination=file['Key']

    #print(destination)
    #print(type(destination))


    response = services.copy_object(Bucket='athiva-target-bucket',CopySource='athiva-training/'+destination,Key=    destination)
    print(response)