from django.shortcuts import render
from utils.decorators import graphic_key
from Skzi.models import *

@graphic_key
def index(request):
    return render(request, 'Main/Index.html')
