def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'This is the periodic Lambda function!'
    }
