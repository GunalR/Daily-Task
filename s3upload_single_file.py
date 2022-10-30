import boto3

service = boto3.client('s3')


response = service.upload_file('C:/Users/User/Desktop/S3.txt', 'athiva-training', 'Gunal/S3.txt')
print(response)