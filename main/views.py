import requests
from django.http import JsonResponse
from django.shortcuts import render

from main.properties.utils_for_views_file import create_patient_request, search_patient_request, \
    create_reception_request, search_reception_request, get_time_table_request, select_specialties_request


def first_page(request):
    return render(request, 'index.html')


def send_create_patient_request(request):
    if request.method == 'POST':
        try:
            result = create_patient_request()

            return JsonResponse({'status': 'success', 'data': result})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


def send_create_reception_request(request):
    if request.method == 'POST':
        try:
            result = create_reception_request()

            return JsonResponse({'status': 'success', 'data': result})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


def send_search_reception_request(request):
    if request.method == 'POST':
        try:
            result = search_reception_request()

            return JsonResponse({'status': 'success', 'data': result})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


def send_search_patient_request(request):
    if request.method == 'GET':
        try:
            result = search_patient_request()

            return JsonResponse({'status': 'success', 'data': result})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


def send_get_time_table_request(request):
    if request.method == 'GET':
        try:
            result = get_time_table_request()

            return JsonResponse({'status': 'success', 'data': result})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


def send_select_specialties_request(request):
    if request.method == 'GET':
        try:
            result = select_specialties_request()

            return JsonResponse({'status': 'success', 'data': result})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
