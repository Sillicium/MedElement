from main.properties.properties import BASE_URL
from main.properties.utils import send_get_request, response_result

url = BASE_URL + "/specialties/v1/linked_to_doctor"

company_code = 772444821619761147

select_specialties_data = {
    'company_code': company_code
}

response = send_get_request(url, select_specialties_data)

print(f"Status code: {response.status_code}")
print("Response text:")
print(response.text)

response_result(response, 'select_specialties_response')
