from django.http import JsonResponse, FileResponse
from django.shortcuts import render

from utils.shortcuts import iredirect
from .forms import *
from .models import *


def otdel_ib(request):
    otdel_id = request.GET.get('otdel')
    return render(request, 'Security/Otdel_IB.html')


def zhurnal(request):
    skzis = Skzi.objects.all()
    return render(request, 'Security/Zhurnal.html', {'skzis': skzis})


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
            return iredirect('security:zhurnal')
        print(form.errors)
        data['form'] = form
    return render(request, 'Security/ZhurnalForm.html', data)
