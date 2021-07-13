import requests

url = "https://www.fast2sms.com/dev/bulkV2"

payload = "message=hiiiii&language=english&route=q&numbers=7606027067"
headers = {
    'authorization': "cKQvLG4lB7DngxkZA0m8IYSiTjXFOaRVHU2d9zu3y6o1pqEwMtVYW9FOoay26E4kNJX1lKxgD5b0Gwdc",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
