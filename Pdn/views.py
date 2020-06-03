from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from .forms import *


def persons_list(request):
    instances = Person.objects.all()
    fakultet = request.GET.get('fakultet')
    podrazd = request.GET.get('podrazd')
    if fakultet and fakultet != '':
        instances = instances.filter(fakultet__id=fakultet)
    if podrazd and podrazd != '':
        instances = instances.filter(podrazd__id=podrazd)
    data = {'instances': instances, 'sogl_raspr': instances.filter(sogl_raspr=True).count(),
            'sogl_obr': instances.filter(soglasie=True).count(), 'fakultets': Fakultet.objects.all(),
            'podrazds': Podrazdelenie.objects.all()}
    return render(request, 'Pdn/PersonsList.html', data)


def person_form(request, id=None):
    person = None
    if id:
        person = Person.objects.get_or_404(id=id)

    form = PersonForm(instance=person)

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect(reverse('pdn:persons_list'))
    return render(request, 'Pdn/PersonForm.html',
                  {'form': form, 'fakultets': Fakultet.objects.all(), 'podrazds': Podrazdelenie.objects.all()})
