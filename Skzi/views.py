from django.http import JsonResponse, FileResponse
from django.shortcuts import render

from utils.shortcuts import iredirect
from utils.word import word_skzi
from .forms import *
from .models import *


def zhurnal(request):
    if request.method == 'POST':
        Skzi.objects.filter(id__in=request.POST.get('id', '').split(',')).update(archive=True)

    skzis = Skzi.objects.filter(archive=False).all()
    if request.GET.get('fiorassilki', '') != '':
        skzis = skzis.filter(to_person__in=request.GET.getlist('fiorassilki'))
    if request.GET.get('action') == 'download':
        path = word_skzi(request, skzis)
        return FileResponse(open(path, 'rb'))
    return render(request, 'Skzi/Zhurnal.html', {'skzis': skzis, 'fio_rassilki_list': FioRassilki.objects.all(),
                                                 'fio_cur': request.GET.get('fiorassilki')})


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
