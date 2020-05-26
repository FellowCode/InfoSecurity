from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from .forms import *


def persons_list(request):
    return render(request, 'Pdn/PersonsList.html', {'instances': Person.objects.all()})


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
    return render(request, 'Pdn/PersonForm.html', {'form': form})