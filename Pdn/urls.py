from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('persons-list/', persons_list, name='persons_list'),
    path('person-form/<id>/', person_form, name='person_form'),
    path('person-form/', person_form, name='person_form'),
    path('otchet/', otchet, name='otchet')

]
