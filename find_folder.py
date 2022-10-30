import boto3

client = boto3.client('s3')
response= client.list_objects(Bucket='athiva-target-bucket',Delimiter='/')
#print(response)
common=response['CommonPrefixes']
print(common)
for i in common:
    print(i['Prefix'])

