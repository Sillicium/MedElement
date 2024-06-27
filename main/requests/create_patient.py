from main.properties.properties import BASE_URL
from main.properties.utils import send_post_request, response_result

url = BASE_URL + "/doctor/v1/patient"
# Данные для создания пациента
name = 'Andrey'
lastname = 'Mishutkin'
middlename = 'Krutoyev'

create_patient_data = {
    'name': name,
    'lastname': lastname,
    'middlename': middlename
}

response = send_post_request(url, create_patient_data)

print(f"Status code: {response.status_code}")
print("Response text:")
print(response.text)

response_result(response, 'create_patient_response')
