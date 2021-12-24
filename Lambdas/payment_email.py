import json, boto3, random
from boto3.dynamodb.conditions import Key
#import requests
#from requests_aws4auth import AWS4Auth

senderEmailId = "prateekmdesai04@gmail.com"


# Lambda execution starts here
def lambda_handler(event, context):
    print(event)
    
    EmailType = event['queryStringParameters']['userEmail']
    product_id = event['queryStringParameters']['pid']
    product_name = event['queryStringParameters']['pname']
    product_price = event['queryStringParameters']['pprice']
    product_desc = event['queryStringParameters']['pdesc']
    
    print(product_id)
    
    dynamo = boto3.resource('dynamodb')
    emailMaster = dynamo.Table('product_info')
    emailResponse = emailMaster.query(
        KeyConditionExpression=Key('product_id').eq(product_id),
        ProjectionExpression='issuer_id,bidder_id'
    )
    
    print(emailResponse)
    for item in  emailResponse['Items']:
        print(item)
        buyer = item['bidder_id']
        seller = item['issuer_id']
        """
        buyerDict = item[0]
        buyer = buyerDict['bidder_id']
        sellerDict = item[1]
        seller = sellerDict['issuer_id']
        """
    
    print(buyer, seller)
    
    
    
    #EmailType = "pm3278@nyu.edu"
    EmailTypeSeller = str(seller)
    msg = "Hello, you have recently sold the following item: \n Product ID: {} \n Product Name: {} \n Product Price: {} \n Product Description: {}".format(product_id, product_name, product_price, product_desc)
    msgBuyer = "Hello, you have recently purchased the following item: \n Product ID: {} \n Product Name: {} \n Product Price: {} \n Product Description: {}".format(product_id, product_name, product_price, product_desc)
    region = 'us-east-1' # For example, us-west-1
    service = 'es'
    credentials = boto3.Session().get_credentials()
    #awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)
    
    ses = boto3.client('ses')
    verifiedResponse = ses.list_verified_email_addresses()
    if EmailTypeSeller not in verifiedResponse['VerifiedEmailAddresses']:
        verifyEmailResponse = ses.verify_email_identity(EmailAddress=EmailTypeSeller)
        print(verifyEmailResponse)
        return
    
    mailResponse = ses.send_email(
        Source=senderEmailId,
        Destination={'ToAddresses': [EmailTypeSeller]},
        Message={
            'Subject': {
                'Data': "NYU Marketplace has a message for you!",
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text': {
                    'Data': msg,
                    'Charset': 'UTF-8'
                },
                'Html': {
                    'Data': msg,
                    'Charset': 'UTF-8'
                }
            }
        }
    )
    
    if buyer != 'None':
        EmailTypeBuyer = buyer
    else:
        EmailTypeBuyer = EmailType
        
    if EmailTypeBuyer not in verifiedResponse['VerifiedEmailAddresses']:
        verifyEmailResponse = ses.verify_email_identity(EmailAddress=EmailTypeBuyer)
        print(verifyEmailResponse)
        return
    
    mailResponseBuyer = ses.send_email(
        Source=senderEmailId,
        Destination={'ToAddresses': [EmailTypeBuyer]},
        Message={
            'Subject': {
                'Data': "NYU Marketplace has a message for you!",
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text': {
                    'Data': msgBuyer,
                    'Charset': 'UTF-8'
                },
                'Html': {
                    'Data': msgBuyer,
                    'Charset': 'UTF-8'
                }
            }
        }
    )
        
    
    dynamo = boto3.resource('dynamodb')
    deleteRecord = dynamo.Table('product_info')
    deleteResponse = deleteRecord.delete_item(
        Key={
            'product_id': product_id,
        }
    )
    
    # Create the response and add some extra content to support CORS
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": '*'
        },
        "isBase64Encoded": False
    }

    response['body'] = "Hello"
    return response
    