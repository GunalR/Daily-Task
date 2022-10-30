import boto3

service=boto3.client('s3')

response=service.list_objects(Bucket='athiva-training')
print(type(response))
print(response)