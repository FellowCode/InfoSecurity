from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('zametki/', zametki, name='zametki'),
    path('zametki/delete/', delete_zametka, name='delete_zametka'),
]