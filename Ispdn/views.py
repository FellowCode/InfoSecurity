from datetime import datetime, timedelta

from django.contrib.admin.models import CHANGE, ADDITION
from django.http import FileResponse, JsonResponse
from django.shortcuts import render

from utils.shortcuts import iredirect, add_log_entry
from .forms import *
from .models import *
from Pdn.models import Person


def select_ispdn(request):
    date_warnings = []
    ispdns = Ispdn.objects.all()
    for ispdn in ispdns:
        td = ispdn.end_date - datetime.date(datetime.now())
        if td < timedelta(days=90):
            date_warnings.append((ispdn, td))
    return render(request, 'Ispdn/SelectIspdn.html', {'ispdns': ispdns, 'date_warnings': date_warnings})


def ispdn(request, ispdn_id):
    ispdn = Ispdn.objects.get_or_404(id=ispdn_id)
    if request.is_ajax() and request.method == 'POST':
        form = IspdnDateForm(request.POST, instance=ispdn)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'OK'})
    return render(request, 'Ispdn/Ispdn.html', {'ispdn': ispdn})


def prikazi(request, ispdn_id=None):
    return instance_list(request, ispdn_id, template='Ispdn/TableList/Prikazi.html', model=Prikaz, field_name='prikaz')


def prikaz_form(request, id=None):
    return form(request, id, template='Ispdn/Forms/PrikazForm.html', model=Prikaz, model_form=PrikazForm,
                reverse_name='prikazi', field_name='prikaz')


def prikaz_download(request, id):
    prikaz = Prikaz.objects.get_or_404(id=id)
    return FileResponse(prikaz.file, filename=prikaz.get_filename())


def instructs(request, ispdn_id=None):
    return instance_list(request, ispdn_id, template='Ispdn/TableList/Instructs.html', model=Instruct, field_name='instruct')


def instruct_form(request, id=None):
    return form(request, id, template='Ispdn/Forms/InstructForm.html', model=Instruct, model_form=InstructForm,
                reverse_name='instructs', field_name='instruct')


def instruct_download(request, id):
    instance = Instruct.objects.get_or_404(id=id)
    return FileResponse(instance.file, filename=get_filename(instance))


def polozhenia(request, ispdn_id=None):
    return instance_list(request, ispdn_id, template='Ispdn/TableList/Polozhenia.html', model=Polozhenie, field_name='polozhenie')


def polozhenie_form(request, id=None):
    return form(request, id, template='Ispdn/Forms/PolozhenieForm.html', model=Polozhenie, model_form=PolozhenieForm,
                reverse_name='polozhenia', field_name='polozhenie')


def polozhenie_download(request, id):
    instance = Polozhenie.objects.get_or_404(id=id)
    return FileResponse(instance.file, filename=get_filename(instance))


def rukovodstva(request, ispdn_id=None):
    return instance_list(request, ispdn_id, template='Ispdn/TableList/Rukovodstva.html', model=Rukovodstvo, field_name='rukovodstvo')


def rukovodstvo_form(request, id=None):
    return form(request, id, template='Ispdn/Forms/RukovodstvoForm.html', model=Rukovodstvo, model_form=RukovodstvoForm,
                reverse_name='rukovodstva', field_name='rukovodstvo')


def rukovodstvo_download(request, id):
    instance = Rukovodstvo.objects.get_or_404(id=id)
    return FileResponse(instance.file, filename=get_filename(instance))


def progob(request, ispdn_id=None):
    return instance_list(request, ispdn_id, template='Ispdn/TableList/ProgOb.html', model=ProgOb, field_name='po')


def progob_form(request, id=None):
    return form(request, id, template='Ispdn/Forms/ProgObForm.html', model=ProgOb, model_form=ProgObForm,
                reverse_name='progob', field_name='po')


def progob_download(request, id):
    instance = ProgOb.objects.get_or_404(id=id)
    return FileResponse(instance.file, filename=get_filename(instance))


def raznoe(request, ispdn_id=None):
    return instance_list(request, ispdn_id, template='Ispdn/TableList/Raznoe.html', model=Raznoe, field_name='raznoe')


def raznoe_form(request, id=None):
    return form(request, id, template='Ispdn/Forms/RaznoeForm.html', model=Raznoe, model_form=RaznoeForm,
                reverse_name='raznoe', field_name='raznoe')


def raznoe_download(request, id):
    instance = Raznoe.objects.get_or_404(id=id)
    return FileResponse(instance.file, filename=get_filename(instance))


def get_filename(instance):
    return instance.file.name.split('/')[-1]


def instance_list(request, ispdn_id, template, model, field_name):
    ispdn = None
    if ispdn_id:
        ispdn = Ispdn.objects.get_or_404(id=ispdn_id)
        instances = getattr(ispdn, field_name).all()
    else:
        instances = model.objects.all()

    ispdns = Ispdn.objects.all()

    return render(request, template, {'instances': instances, 'ispdn': ispdn, 'ispdns': ispdns})


def form(request, id, template, model, model_form, reverse_name, field_name):
    data = {'form': model_form(), 'persons': Person.objects.all(), 'source': request.GET.get('source'),
            'ispdns': Ispdn.objects.all(), 'source_ispdn': Ispdn.objects.get_or_none(id=request.GET.get('source'))}
    if data['source']:
        data['source'] = int(data['source'])
    instance = None
    if id:
        instance = model.objects.get_or_404(id=id)
        data['instance_ispdns'] = list(instance.ispdns.values_list('id', flat=True).all())
        data['form'] = model_form(instance=instance)

    if request.method == 'POST':
        ispdns_ids = list(map(int, request.POST.getlist('ispdn', [])))
        form = model_form(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            if instance:
                act_flag = CHANGE
            else:
                act_flag = ADDITION
            instance = form.save()
            for ispdn in data['ispdns']:
                if ispdn.id in ispdns_ids:
                    getattr(ispdn, field_name).add(instance)
                else:
                    getattr(ispdn, field_name).remove(instance)
                ispdn.save()
            add_log_entry(request.user, instance, act_flag)
            if data['source']:
                return iredirect(f'ispdn:{reverse_name}', ispdn_id=data['source'])
            return iredirect(f'ispdn:{reverse_name}_all')
    return render(request, template, data)
