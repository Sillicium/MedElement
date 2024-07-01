from main.properties.properties import BASE_URL
from main.properties.utils import send_post_request, response_result


url = BASE_URL + "/v1/doctor/reception"

patient_code = 525816101719390250
specialist_code = 911426371551332205
company_cabinet_code = 166903901619761652
start_time = '31.05.2022 10:00'
end_time = '31.05.2022 11:30'
description = 'qwerty'

date_time_data = {
    'patient_code': patient_code,
    'specialist_code': specialist_code,
    'company_cabinet_code': company_cabinet_code,
    'starttime': start_time,
    'endtime': end_time,
    'description': description
}

response = send_post_request(url, date_time_data)

print(f"Status code: {response.status_code}")
print("Response text:")
print(response.text)

response_result(response, 'create_reception_response')
