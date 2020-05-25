from django.http import JsonResponse, FileResponse
from django.shortcuts import render

from utils.shortcuts import iredirect
from .forms import *
from .models import *


def zhurnal(request):
    skzis = Skzi.objects.all()
    return render(request, 'Skzi/Zhurnal.html', {'skzis': skzis})


def zhurnal_form(request, id=None):
    data = {'skzi_names': SkziName.objects.all(),
            'fio_rassilki': FioRassilki.objects.all(),
            'organs_crypto': OrganCrypto.objects.all(),
            'form': SkziForm()}
    skzi = None
    if id:
        skzi = Skzi.objects.get_or_404(id=id)
        data['form'] = SkziForm(instance=skzi)
    if request.method == 'POST':
        if skzi:
            form = SkziForm(request.POST, instance=skzi)
        else:
            form = SkziForm(request.POST)
        if form.is_valid():
            form.save()
            return iredirect('skzi:zhurnal')
        print(form.errors)
        data['form'] = form
    return render(request, 'Skzi/ZhurnalForm.html', data)
