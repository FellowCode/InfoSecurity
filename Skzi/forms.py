from django.forms import ModelForm
from .models import *

class SkziForm(ModelForm):
    class Meta:
        model = Skzi
        exclude = ['id']


class SkziNameForm(ModelForm):
    class Meta:
        model = SkziName
        exclude = ['id']


class FioRassilkiForm(ModelForm):
    class Meta:
        model = FioRassilki
        exclude = ['id']



