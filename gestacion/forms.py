from django import forms
from .models import Madre, Parto, RecienNacido

class MadreForm(forms.ModelForm):
    class Meta:
        model = Madre
        fields = "__all__" #Incluye todos los campos del modelo en el formulario
        widgets = {
            "direccion": forms.TextInput(attrs={"placeholder":"Calle, número, ciudad"}),
            "telefono_contacto": forms.TextInput(attrs={"placeholder":"+56 9 ...."}),
        }

class PartoForm(forms.ModelForm):
    class Meta:
        model = Parto
        fields = "__all__" #Incluye todos los campos del modelo en el formulario
        widgets = {
            "fecha_parto": forms.DateInput(attrs={"type":"date"}),
            "observaciones": forms.Textarea(attrs={"rows":3}),
        }

class RNForm(forms.ModelForm):
    class Meta:
        model = RecienNacido  #el formulario se basa en el modelo RecienNacido.
        fields = "__all__" #Incluye todos los campos del modelo en el formulario
