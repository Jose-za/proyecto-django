from django import forms
from .models import Alumnos

class Usuario(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['matricula', 'nombre', 'carrera', 'turno']