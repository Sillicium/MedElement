import base64
import json
import requests

username = '24b0c821ffb65f3c15dc1071b4c6812a'
password = '63f4805a42886'

base64_string = f'{username}:{password}'.encode('ascii')
base64_credentials = base64.b64encode(base64_string).decode('ascii')
headers = {
    'Authorization': f'Basic {base64_credentials}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

# response = requests.post( headers=headers)
