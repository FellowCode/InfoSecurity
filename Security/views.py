from django.shortcuts import render
from .forms import *
from .models import *


def otdel_ib(request):
    otdel_id = request.GET.get('otdel')
    otdel = OtdelIR.objects.get_or_404(id=otdel_id)
    request.session['otdel'] = otdel
    return render(request, 'Security/Otdel_IB.html', {'otdel': otdel})

def zhurnal(request):
    skzis = Skzi.objects.all()
    return render(request, 'Security/Zhurnal.html', {'skzis': skzis})


def zhurnal_form(request):
    skzi_names = SkziName.objects.all()
    persons = Person.objects.all()
    form = SkziForm()
    return render(request, 'Security/ZhurnalForm.html', {'form': form, 'skzi_names': skzi_names, 'person': persons})
