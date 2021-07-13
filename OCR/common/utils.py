import requests
import json

def sendTextMessage(message,contact):
    url = "https://www.fast2sms.com/dev/bulkV2"
    payload = "sender_id=TXTIND&message="+message+"&route=v3&numbers="+contact
    headers = {
    'authorization': "cKQvLG4lB7DngxkZA0m8IYSiTjXFOaRVHU2d9zu3y6o1pqEwMtVYW9FOoay26E4kNJX1lKxgD5b0Gwdc",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    dict_data = json.loads(response.text)

    return dict_data['return']