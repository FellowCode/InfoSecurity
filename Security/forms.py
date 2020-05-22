from django.forms import ModelForm
from .models import Skzi

class SkziForm(ModelForm):
    class Meta:
        model = Skzi

        fields = ['name']
