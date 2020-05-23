from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', select_ispdn, name='select'),
    path('<ispdn_id>/', ispdn, name='menu'),
    path('<ispdn_id>/prikazi/', prikazi, name='prikazi'),
    path('<ispdn_id>/prikaz-form/', prikaz_form, name='prikaz_form'),
    path('<ispdn_id>/prikaz-form/<id>/', prikaz_form, name='prikaz_form_id'),
    path('prikaz-download/<id>/', prikaz_download, name='prikaz_download'),
]
