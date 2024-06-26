import base64

username = 'd4eaa832f927e761627b31dc965d7702'
password = '608b982d8518f'

base64_string = f'{username}:{password}'.encode('ascii')
base64_credentials = base64.b64encode(base64_string).decode('ascii')
headers = {
    'Authorization': f'Basic {base64_credentials}',
    'Content-Type': 'application/x-www-form-urlencoded'
}
