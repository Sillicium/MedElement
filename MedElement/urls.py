"""
URL configuration for MedElement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page, name='first_page'),


    path('create_patient_form/', views.create_patient_form, name='create_patient_form'),
    path('create_patient/', views.create_patient, name='create_patient'),


    path('create_patient_form/', views.search_patient_form, name='search_patient_form'),
    path('create_patient/', views.search_patient, name='search_patient'),


    path('create_reception_form/', views.create_reception_form, name='create_reception_form'),
    path('create_reception/', views.create_reception, name='create_reception'),


    path('search_reception_form/', views.search_reception_form, name='search_reception_form'),
    path('search_reception/', views.search_reception, name='search_reception'),


    path('select_specialties_form/', views.select_specialties_form, name='select_specialties_form'),
    path('select_specialties/', views.select_specialties, name='select_specialties'),


    path('time_table_form/', views.time_table_form, name='time_table_form'),
    path('time_table/', views.time_table, name='time_table'),



]
