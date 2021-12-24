import json

def lambda_handler(event, context):
    print("The incoming data is", json.dumps(event))
    bucket = event['Records'][0]['s3']['bucket']['name']
    photo = event['Records'][0]['s3']['object']['key']
    print("\nThe name of the image: ", photo)
    print("\nThe name of the bucket: ", bucket)
    link = "https://nyu-items-store.s3.amazonaws.com/"+photo
    
    print("\n Final Link is: ", link)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
