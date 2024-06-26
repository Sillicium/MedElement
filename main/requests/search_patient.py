from main.properties.properties import BASE_URL
from main.properties.utils import send_get_request, response_result

url = BASE_URL + "/doctor/v1/patients"


name = 'Andrey'
lastname = 'Mishutkin'
middlename = 'Krutoyev'

search_patient_data = {
    'name': name,
    'lastname': lastname,
    'middlename': middlename
}

response = send_get_request(url, search_patient_data)

print(f"Status code: {response.status_code}")
print("Response text:")
print(response.text)


response_result(response, 'search_patient_response')
