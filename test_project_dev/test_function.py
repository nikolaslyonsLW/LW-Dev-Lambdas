import json

def lambda_handler(event, context):
    # TODO Implement Logic
    variable = "this is a test 2"
    return {{
        
        'statusCode': 200,
        'body': json.dumps('Create new lambda function')
    }}
