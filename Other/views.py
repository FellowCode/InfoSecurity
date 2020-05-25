from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Zametka
from .forms import *


def zametki(request):
    if request.method == 'POST':
        form = ZametkaForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'Other/Zametki.html', {'zametki': Zametka.objects.all()})


def delete_zametka(request):
    if request.is_ajax() and request.method == 'POST':
        Zametka.objects.get_or_404(id=request.POST.get('id')).delete()
        return redirect(reverse('other:zametki'))
    raise Http404