from django.http import FileResponse
from django.shortcuts import render

from utils.shortcuts import iredirect
from .forms import *


def select_ispdn(request):
    return render(request, 'Ispdn/SelectIspdn.html', {'ispdns': Ispdn.objects.all()})


def ispdn(request, ispdn_id):
    return render(request, 'Ispdn/Ispdn.html', {'ispdn_id': ispdn_id})


def prikazi(request, ispdn_id):
    prikazi = Ispdn.objects.get_or_404(id=ispdn_id).prikaz.all()
    return render(request, 'Ispdn/Prikazi.html', {'prikazi': prikazi, 'ispdn_id': ispdn_id})


def prikaz_form(request, ispdn_id, id=None):
    ispdn = Ispdn.objects.get_or_404(id=ispdn_id)
    data = {'ispdn_id': ispdn_id, 'form': PrikazForm(), 'persons': Person.objects.all(),
            'alter_prikazi': Prikaz.objects.exclude(id__in=ispdn.prikaz.values('id').all())}

    prikaz = None
    if id:
        prikaz = Prikaz.objects.get_or_404(id=id)
        data['form'] = PrikazForm(instance=prikaz)

    if request.method == 'POST':
        form = PrikazForm(request.POST, request.FILES, instance=prikaz)
        if form.is_valid():
            prikaz = form.save()
            ispdn.prikaz.add(prikaz)
            ispdn.save()
            return iredirect('ispdn:prikazi', ispdn_id=ispdn_id)
        print(form.errors)
    return render(request, 'Ispdn/PrikazForm.html', data)


def prikaz_download(request, id):
    prikaz = Prikaz.objects.get_or_404(id=id)
    return FileResponse(prikaz.file, filename=prikaz.get_filename())
