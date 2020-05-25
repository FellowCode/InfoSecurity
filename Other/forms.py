from django.forms import ModelForm
from .models import *


class ZametkaForm(ModelForm):
    class Meta:
        model = Zametka
        fields = ['name', 'content']
