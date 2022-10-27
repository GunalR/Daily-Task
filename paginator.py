import boto3

# Create a client
service = boto3.client('s3')

# Create a reusable Paginator
response = service.get_paginator('list_objects')

# Create a PageIterator from the Paginator
page_iterator = response.paginate(Bucket='athiva-training')

for page in page_iterator:
    #print(page['Contents'])
    for key in page['Contents']:
        print(key['Key'])

