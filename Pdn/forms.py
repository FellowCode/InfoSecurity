from django.forms import ModelForm
from .models import *


class PersonForm(ModelForm):
    class Meta:
        model = Person
        exclude = ['id']