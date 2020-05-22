from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('zhurnal/', zhurnal, name='zhurnal'),
    path('zhurnal-form/', zhurnal_form, name='zhurnal_form'),
    path('otdel/', otdel_ib, name='otdel'),
]
