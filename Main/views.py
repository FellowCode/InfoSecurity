from django.shortcuts import render
from utils.decorators import graphic_key
from Security.models import *

@graphic_key
def index(request):
    otdels = OtdelIR.objects.all()
    return render(request, 'Main/Index.html', {'otdels': otdels})
