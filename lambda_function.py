import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = 'assignment-6a-s3-demo-bucket'
    response = s3.list_objects_v2(Bucket=bucket)
    objects = [obj['Key'] for obj in response.get('Contents', [])]
    print(f"Found objects: {objects}")
    return {
        'statusCode': 200,
        'body': str(objects)
    }
