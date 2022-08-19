
from dataclasses import fields
from django import forms

from .models import *

class formEquipos(forms.ModelForm):
    class Meta:
        model = Equipos
        fields = "__all__"
    