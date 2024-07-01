import datetime
import json

import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from main.properties.properties import BASE_URL
from main.properties.utils import send_post_request, create_response_json_file, send_get_request
from main.properties.utils_for_views_file import create_patient_request, search_patient_request, \
    create_reception_request, search_reception_request, get_time_table_request, select_specialties_request


def first_page(request):
    return render(request, 'index.html')


def create_patient_form(request):
    return render(request, 'page_forms/create_patient_form.html')


def search_patient_form(request):
    return render(request, 'page_forms/search_patient_form.html')


def create_reception_form(request):
    return render(request, 'page_forms/create_reception_form.html')


def search_reception_form(request):
    return render(request, 'page_forms/search_reception_form.html')


def select_specialties_form(request):
    return render(request, 'page_forms/select_specialties.html')


def time_table_form(request):
    return render(request, 'page_forms/time_table_form.html')


def create_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        middlename = request.POST.get('middlename')
        email = request.POST.get('email')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        iin = request.POST.get('iin')

        request_url = BASE_URL + "/doctor/v1/patient"

        create_patient_data = {
            'name': name,
            'lastname': lastname,
            'middlename': middlename,
            'email': email,
            'birthday': birthday,
            'gender': gender,
            'phone': phone,
            'iin': iin
        }

        response = send_post_request(request_url, create_patient_data)

        if response.status_code in [200, 201]:
            response_json = response.json()
            create_response_json_file('create_patient_response', response_json)
            return JsonResponse(response_json)
        else:
            return HttpResponse(f"Error: Received status code {response.status_code}", status=response.status_code)

    return redirect('first_page')


def search_patient(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        lastname = request.GET.get('lastname')
        middlename = request.GET.get('middlename')
        email = request.GET.get('email')
        birthday = request.GET.get('birthday')
        gender = request.GET.get('gender')
        phone = request.GET.get('phone')
        iin = request.GET.get('iin')

        request_url = BASE_URL + "/doctor/v1/patients"

        search_patient_data = {
            'name': name,
            'lastname': lastname,
            'middlename': middlename,
            'email': email,
            'birthday': birthday,
            'gender': gender,
            'phone': phone,
            'iin': iin
        }

        response = send_get_request(request_url, search_patient_data)

        if response.status_code in [200, 201]:
            response_json = response.json()
            create_response_json_file('search_patient_response', response_json)
            return JsonResponse(response_json)
        else:
            return HttpResponse(f"Error: Received status code {response.status_code}", status=response.status_code)

    return redirect('first_page')


def create_reception(request):
    if request.method == 'POST':
        patient_code = request.POST.get('patient_code')
        specialist_code = request.POST.get('specialist_code')
        company_cabinet_code = request.POST.get('company_cabinet_code')
        start_time = request.POST.get('starttime')
        end_time = request.POST.get('endtime')  # Assuming the key is 'endtime'
        description = request.POST.get('description')

        request_url = BASE_URL + "/v1/doctor/reception"

        symbols_to_remove = "T"

        for symbol in symbols_to_remove:
            formatted_start_time = start_time.replace(symbol, " ")
            formatted_end_time = end_time.replace(symbol, " ")

        date_time_data = {
            'patient_code': patient_code,
            'specialist_code': specialist_code,
            'company_cabinet_code': company_cabinet_code,
            'starttime': formatted_start_time,
            'endtime': formatted_end_time,
            'description': description
        }

        response = send_post_request(request_url, date_time_data)

        if response.status_code in [200, 201]:
            response_json = response.json()
            create_response_json_file('create_reception_response', response_json)
            return JsonResponse(response_json)
        else:
            return HttpResponse(f"Error: Received status code {response.status_code}", status=response.status_code)

    return redirect('first_page')


def search_reception(request):
    if request.method == 'POST':
        patient_code = request.POST.get('patient_code')
        specialist_code = request.POST.get('specialist_code')
        company_cabinet_code = request.POST.get('company_cabinet_code')
        start_time = request.POST.get('starttime')
        end_time = request.POST.get('endtime')
        description = request.POST.get('description')

        date_time_data = {
            # 'patient_code': patient_code,
            # 'specialist_code': specialist_code,
            # 'company_cabinet_code': company_cabinet_code,
            'begin_datetime': start_time,
            'end_datetime': end_time,
            # 'description': description
        }

        request_url = BASE_URL + "/v2/doctor/reception/search"

        response = send_post_request(request_url, date_time_data)

        if response.status_code in [200, 201]:
            response_json = response.json()
            create_response_json_file('search_reception_response', response_json)
            return JsonResponse(response_json)
        else:
            return HttpResponse(f"Error: Received status code {response.status_code}", status=response.status_code)

    return redirect('first_page')


def select_specialties(request):
    if request.method == 'GET':
        company_code = request.GET.get('company_code')

        select_specialties_data = {
            'company_code': company_code
        }

        request_url = BASE_URL + "/specialties/v1/linked_to_doctor"

        response = send_get_request(request_url, select_specialties_data)

        if response.status_code in [200, 201]:
            response_json = response.json()
            create_response_json_file('select_specialties_response', response_json)
            return JsonResponse(response_json, safe=False)
        else:
            return HttpResponse(f"Error: Received status code {response.status_code}", status=response.status_code)

    return redirect('first_page')


def time_table(request):
    if request.method == 'GET':
        date = request.GET.get('date')

        request_url = BASE_URL + "/v1/specialists/timetable"

        search_patient_data = {
            'date': date
        }

        response = send_get_request(request_url, search_patient_data)

        if response.status_code in [200, 201]:
            response_json = response.json()
            create_response_json_file('time_table_response', response_json)
            return JsonResponse(response_json)
        else:
            return HttpResponse(f"Error: Received status code {response.status_code}", status=response.status_code)

    return redirect('first_page')
