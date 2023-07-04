import json
import boto3
import base64

def lambda_handler(event, context):
    key = event['s3_key']
    bucket_name = event['s3_bucket']
    tmp_directory = '/tmp/image.png'
    
    # download image into tmp directory
    s3 = boto3.resource('s3', region_name='us-east-1')
    s3.meta.client.download_file(bucket_name, key, tmp_directory)
    
    # base64 it
    with open(tmp_directory, 'rb') as f:
        image_data = base64.b64encode(f.read())
    
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket_name,
            "s3_key": key,
            "inferences": []
        }
    }
