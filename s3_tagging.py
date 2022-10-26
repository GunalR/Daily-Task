import boto3
service=boto3.client('s3')
response=service.list_objects(Bucket='athiva-training',Prefix='Gunal/')

for objects in (response['Contents']):
    #print(objects['Key'])
    objects_path=objects['Key']

    response = service.put_object_tagging( Bucket='athiva-training',Key=objects_path,Tagging={'TagSet':[{'Key':'Owner','Value':'Gunal'},{'Key':'Task','Value':'s3-training'}]})
    print(response)