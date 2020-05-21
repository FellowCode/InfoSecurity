from django.shortcuts import render
from utils.decorators import graphic_key


@graphic_key
def index(request):
    return render(request, 'Main/Index.html')
