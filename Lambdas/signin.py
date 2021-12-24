import json, sys, base64, datetime, boto3, random
from boto3.dynamodb.conditions import Key
import urllib.parse

dynamo = boto3.client('dynamodb')


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


        userEmailList = formDict['SignInEmail']
        userEmail = userEmailList[0]
        
        userPasswordList = formDict['SignInPassword']
        userPassword = userPasswordList[0]
        
        
        print(userEmail, userPassword)
        
        client = boto3.resource('dynamodb')
        SignIn = client.Table('user_info')
        SignInPassword = SignIn.query(
            KeyConditionExpression=Key('user_email').eq(userEmail),
            ProjectionExpression='user_password',
            ConsistentRead=True
        )
        
        
        print("Sign in Password is ", SignInPassword)
        
        
        if len(SignInPassword['Items']) == 0:
            response['body'] = "Account does not exist for this user. You need to sign up first!"
        else:
            print(userPassword)
            temp1 = SignInPassword['Items']
            temp2 = temp1[0]
            print(temp2)
            temp3 = temp2['user_password']
            print(temp3)
            if (userPassword == temp3):
                response['body'] = "Login Successful"
            else:
                response['body'] = "Login Failed"
            

    except Exception as e:
        print("Exception is", str(e))
        response['statusCode'] = 500;

    print(response)
    return response
