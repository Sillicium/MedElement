from main.properties.properties import BASE_URL
from main.properties.utils import send_post_request, response_result

url = BASE_URL + "/v2/doctor/reception/search"

begin_datetime = '11.06.2024'
end_datetime = '12.06.2024'

date_time_data = {
    'begin_datetime': begin_datetime,
    'end_datetime': end_datetime
}

response = send_post_request(url, date_time_data)

print(f"Status code: {response.status_code}")
print("Response text:")
print(response.text)


response_result(response, 'reception_search_response')
