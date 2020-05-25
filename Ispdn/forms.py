from django.forms import ModelForm
from .models import *


class IspdnDateForm(ModelForm):
    class Meta:
        model = Ispdn
        fields = ['start_date', 'end_date']


class PrikazForm(ModelForm):
    class Meta:
        model = Prikaz
        exclude = ['id']


class InstructForm(ModelForm):
    class Meta:
        model = Instruct
        exclude = ['id']


class RukovodstvoForm(ModelForm):
    class Meta:
        model = Rukovodstvo
        exclude = ['id']


class PolozhenieForm(ModelForm):
    class Meta:
        model = Polozhenie
        exclude = ['id']


class ProgObForm(ModelForm):
    class Meta:
        model = ProgOb
        exclude = ['id']


class RaznoeForm(ModelForm):
    class Meta:
        model = Raznoe
        exclude = ['id']