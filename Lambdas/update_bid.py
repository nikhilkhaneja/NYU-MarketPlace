import json, sys, base64, datetime, boto3, random
import urllib.parse

dynamo = boto3.resource('dynamodb')


def lambda_handler(event, context):
    print("Lister version v1. Event:", event)
    response = {
        "statusCode": 200,
        "statusDescription": "200 OK",
        "isBase64Encoded": False,
        "headers": {
            "Content-Type": "text/html; charset=utf-8"
        }
    }

    try:
        encBodyData = event['body']
        print('Data1: ', encBodyData)
        bodyData = base64.b64decode(encBodyData)
        encFormData = bodyData.decode('utf-8')
        print('Data2: ', encFormData)
        formDict = urllib.parse.parse_qs(encFormData)
        print('Data3: ', formDict)
        
        if 'queryStringParameters' in event and 'p' in event['queryStringParameters']:
            productId = event['queryStringParameters']['p']
        
        
        bidderName = formDict['name'][0]
        bidderID = formDict['email'][0]
        bidderPhone = formDict['phone'][0]
        bidRate = formDict['bidprice'][0]
        
        table = dynamo.Table('product_info')
        
        dynResp = table.update_item(
            Key={'product_id': productId},
            UpdateExpression="set bidder_id = :val1, bidder_phone = :val2, bidder_name = :val3, bidder_price = :val4",
            ExpressionAttributeValues={
                ':val1': bidderID,
                ':val2': bidderPhone,
                ':val3': bidderName,
                ':val4': bidRate
            },
            ReturnValues="UPDATED_NEW"
        )
        
    except Exception as e:
        print("Exception is", str(e))
        response['statusCode'] = 500;

    print(response)
    return response
