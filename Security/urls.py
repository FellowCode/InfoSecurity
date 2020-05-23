from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('zhurnal/', zhurnal, name='zhurnal'),
    path('zhurnal-form/<id>/', zhurnal_form, name='zhurnal_form_id'),
    path('zhurnal-form/', zhurnal_form, name='zhurnal_form'),
]
