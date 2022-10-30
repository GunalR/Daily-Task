import boto3

service=boto3.client('s3')

response=service.list_objects(Bucket='athiva-training')

total=0
for key in (response['Contents']):
    #print(key)
    #print(type(key))
    key_values= key['Key']
    #print(key_values)
    #print(type(key_values))
    total=total+1
print("The total files is:",total)