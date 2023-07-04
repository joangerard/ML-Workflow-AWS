import json
import boto3
import base64

def lambda_handler(event, context):

    endpoint = 'image-classification-2023-07-04-16-00-18-763'
    runtime = boto3.Session().client('sagemaker-runtime')
    image = base64.b64decode(event['image_data'])
    response = runtime.invoke_endpoint(EndpointName=endpoint, ContentType = 'image/png', Body = image)
    predictions = json.loads(response['Body'].read().decode())

    event['inferences'] = predictions
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
