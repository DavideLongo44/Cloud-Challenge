import json

def lambda_handler(event, context):
    # Implementa la logica per elaborare l'evento Lambda
    # Implement the logic to process the Lambda event
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
