from main.properties.properties import BASE_URL
from main.properties.utils import send_get_request, response_result

url = BASE_URL + "/v1/specialists/timetable"

date = '31.12.2017'

search_patient_data = {
    'date': date
}

response = send_get_request(url, search_patient_data)

print(f"Status code: {response.status_code}")
print("Response text:")
print(response.text)


response_result(response, 'get_time_table_response')

