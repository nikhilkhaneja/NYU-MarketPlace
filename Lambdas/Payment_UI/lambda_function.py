import html_page, json

def lambda_handler(event, context):
    print("The incoming data is", json.dumps(event))
    
    response = {
        "statusCode": 200,
        "statusDescription": "200 OK",
        "isBase64Encoded": False,
        "headers": {
            "Content-Type": "text/html; charset=utf-8"
        }
    }

    response['body'] = html_page.payment()
    return response

