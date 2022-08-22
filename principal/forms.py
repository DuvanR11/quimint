
from dataclasses import fields
from django import forms
from django.core.validators import RegexValidator

from .models import *
class formEquipos(forms.ModelForm):
    # fecha = forms.DateField(
    #     label='Fecha',
    #     validators=[RegexValidator(r'^[DdMmYy]{6}$',
    #     message="solo se permite fecha")],
    #     required=True,
    #     widget=forms.TextInput(attrs={'placeholder':'fecha'}))      
                    
    repuesto = forms.CharField(
        label='Repuesto', min_length=3, max_length=30,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message="solo se permite fecha")],
        widget=forms.TextInput(attrs={'placeholder':'Repuesto'}))
    
    class Meta:
        model = Equipos
        fields = "__all__"
    
class formSuministros(forms.ModelForm):
    # fecha = forms.DateField(
    #     label='Fecha',
    #     validators=[RegexValidator(r'^[DdMmYy]{6}$',
    #     message="solo se permite fecha")],
    #     required=True,
    #     widget=forms.TextInput(attrs={'placeholder':'fecha'}))      
                    
    # repuesto = forms.CharField(
    #     label='Repuesto', min_length=3, max_length=30,
    #     validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
    #     message="solo se permite fecha")],
    #     widget=forms.TextInput(attrs={'placeholder':'Repuesto'}))
    
    class Meta:
        model = Suministros
        fields = "__all__"
        
        
class formHerramientas(forms.ModelForm):
    # fecha = forms.DateField(
    #     label='Fecha',
    #     validators=[RegexValidator(r'^[DdMmYy]{6}$',
    #     message="solo se permite fecha")],
    #     required=True,
    #     widget=forms.TextInput(attrs={'placeholder':'fecha'}))      
                    
    # repuesto = forms.CharField(
    #     label='Repuesto', min_length=3, max_length=30,
    #     validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
    #     message="solo se permite fecha")],
    #     widget=forms.TextInput(attrs={'placeholder':'Repuesto'}))
    
    class Meta:
        model = Herramientas
        fields = "__all__"