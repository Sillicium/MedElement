from main.properties.properties import BASE_URL
from main.properties.utils import send_post_request, response_result, send_get_request


def create_patient_request():
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

    if response.status_code in [200, 201]:
        return response.json()
    else:
        response.raise_for_status()


def search_patient_request():
    url = BASE_URL + "/doctor/v1/patients"

    # Данные для создания пациента
    name = 'Andrey'
    lastname = 'Mishutkin'
    middlename = 'Krutoyev'

    search_patient_data = {
        'name': name,
        'lastname': lastname,
        'middlename': middlename
    }

    response = send_get_request(url, search_patient_data)

    if response.status_code in [200, 201]:
        return response.json()
    else:
        response.raise_for_status()


def create_reception_request():
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

    if response.status_code in [200, 201]:
        return response.json()
    else:
        response.raise_for_status()


def search_reception_request():

    url = BASE_URL + "/v2/doctor/reception/search"

    begin_datetime = '11.06.2024'
    end_datetime = '12.06.2024'

    date_time_data = {
        'begin_datetime': begin_datetime,
        'end_datetime': end_datetime
    }

    response = send_post_request(url, date_time_data)

    if response.status_code in [200, 201]:
        return response.json()
    else:
        response.raise_for_status()


def get_time_table_request():
    url = BASE_URL + "/v1/specialists/timetable"

    date = '31.12.2017'

    search_patient_data = {
        'date': date
    }

    response = send_get_request(url, search_patient_data)
    if response.status_code in [200, 201]:
        return response.json()
    else:
        response.raise_for_status()


def select_specialties_request():
    url = BASE_URL + "/specialties/v1/linked_to_doctor"

    company_code = 772444821619761147

    select_specialties_data = {
        'company_code': company_code
    }

    response = send_get_request(url, select_specialties_data)

    if response.status_code in [200, 201]:
        return response.json()
    else:
        response.raise_for_status()
