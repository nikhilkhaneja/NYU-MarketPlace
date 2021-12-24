import json
import csv
import boto3

def lambda_handler(event, context):
    region = 'us-east-1'
    record_list = []
    
    try:
        s3 = boto3.client('s3')
        
        dynamodb = boto3.client('dynamodb',region_name = region)
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        print('Bucket: ', bucket, ' Key: ', key)
        
        csv_file = s3.get_object(Bucket = bucket, Key = key)
        
        record_list = csv_file['Body'].read().decode('utf-8').split('\n')
        
        csv_reader = csv.reader(record_list, delimiter=',', quotechar='"')
        
        # for row in csv_reader:
        #     product_id = row[0]
        #     product_name = row[1]
        #     product_type = row[2]
        #     product_desc = row[3]
        #     product_price = row[4]
        #     issuer_id = row[5]
        #     bid_type = row[6]
        #     bid_expiry = row[7]
        #     bid_rate = row[8]
        #     product_url = row[9]
        #     timestamp = row[10]
            
        #     add_to_db = dynamodb.put_item(
        #         TableName = 'product_info',
        #         Item = {
        #             'product_id': {'S': str(product_id)},
        #             'product_name': {'S': str(product_name)},
        #             'product_type': {'S': str(product_type)},
        #             'product_desc': {'S': str(product_desc)},
        #             'product_price': {'S': str(product_price)},
        #             'issuer_id': {'S': str(issuer_id)},
        #             'bid_type': {'S': str(bid_type)},
        #             'bid_expiry': {'S': str(bid_expiry)},
        #             'bid_rate': {'S': str(bid_rate)},
        #             'product_url': {'S': str(product_url)},
        #             'timestamp': {'S': str(timestamp)},
        #         })
        
        for row in csv_reader:
            user_email = row[0]
            user_name = row[1]
            user_contact = row[2]
            user_password = row[3]
            user_createdAt = row[4]
            
            add_to_db = dynamodb.put_item(
                TableName = 'user_info',
                Item = {
                    'user_email': {'S': str(user_email)},
                    'user_name': {'S': str(user_name)},
                    'user_contact': {'S': str(user_contact)},
                    'user_password': {'S': str(user_password)},
                    'user_createdAt': {'S': str(user_createdAt)},
                })
                
        
    except Exception as e:
        print(str(e))
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
