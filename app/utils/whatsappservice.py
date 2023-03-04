import requests
import json
import os

def SendMessageWhatsapp(data):
    try:
        token = os.getenv("TOKEN")
        api_url= os.getenv("API_URL")
        headers = {"Content-Type": "application/json", "Authorization":f"Bearer {token}"}
        response = requests.post(api_url, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            return True
        return False
    except Exception as e:
        print(e)
        return False

