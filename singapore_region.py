import boto3

service=boto3.client('s3',region_name='ap-south-1')


response=service.list_objects(Bucket='athiva-target-bucket')
#print(response)

for file in (response['Contents']):
    #print(file)
    #print(file['Key'])
    #strr=str(file)
    #print(type(file))
    services=boto3.client('s3',region_name='ap-southeast-1')
    response1=services.put_object(Bucket='differentregionbucket',Key=file['Key'])
    print(response1)