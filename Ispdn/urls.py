from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', select_ispdn, name='select'),
    # Приказы
    path('prikazi/', prikazi, name='prikazi_all'),
    path('prikaz-form/', prikaz_form, name='prikaz_form'),
    path('prikaz-form/<id>/', prikaz_form, name='prikaz_form_id'),
    path('<ispdn_id>/prikazi/', prikazi, name='prikazi'),
    path('prikaz-download/<id>/', prikaz_download, name='prikaz_download'),
    # Инструкции
    path('instructs/', instructs, name='instructs_all'),
    path('instruct-form/', instruct_form, name='instruct_form'),
    path('instruct-form/<id>/', instruct_form, name='instruct_form_id'),
    path('<ispdn_id>/instructs/', instructs, name='instructs'),
    path('instruct-download/<id>/', instruct_download, name='instruct_download'),
    # Положения
    path('polozhenia/', polozhenia, name='polozhenia_all'),
    path('polozhenie-form/', polozhenie_form, name='polozhenie_form'),
    path('polozhenie-form/<id>/', polozhenie_form, name='polozhenie_form_id'),
    path('<ispdn_id>/polozhenia/', polozhenia, name='polozhenia'),
    path('polozhenie-download/<id>/', polozhenie_download, name='polozhenie_download'),
    # Руководства
    path('rukovodstva/', rukovodstva, name='rukovodstva_all'),
    path('rukovodstvo-form/', rukovodstvo_form, name='rukovodstvo_form'),
    path('rukovodstvo-form/<id>/', rukovodstvo_form, name='rukovodstvo_form_id'),
    path('<ispdn_id>/rukovodstva/', rukovodstva, name='rukovodstva'),
    path('rukovodstvo-download/<id>/', rukovodstvo_download, name='rukovodstvo_download'),
    # Прог об
    path('progob/', progob, name='progob_all'),
    path('progob-form/', progob_form, name='progob_form'),
    path('progob-form/<id>/', progob_form, name='progob_form_id'),
    path('<ispdn_id>/progob/', progob, name='progob'),
    path('progob-download/<id>/', progob_download, name='progob_download'),
    path('<ispdn_id>/', ispdn, name='menu'),
]
