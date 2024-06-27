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
from django.urls import path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page),
    path('create_patient/', views.send_create_patient_request, name='create_patient'),
    path('search_patient/', views.send_search_patient_request, name='search_patient'),
    path('create_reception/', views.send_create_reception_request, name='create_reception'),
    path('search_reception/', views.send_search_reception_request, name='search_reception'),
    path('time_table/', views.send_get_time_table_request, name='time_table'),
    path('select_specialties/', views.send_select_specialties_request, name='select_specialties'),
]
