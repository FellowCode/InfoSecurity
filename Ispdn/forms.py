from django.forms import ModelForm
from Security.models import *


class PrikazForm(ModelForm):
    class Meta:
        model = Prikaz
        exclude = ['id']


class InstruztForm(ModelForm):
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