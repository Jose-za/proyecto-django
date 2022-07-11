from django import forms
from .models import ComentarioContacto, Alumnos

class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ['usuario', 'mensaje']

class Usuario(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['matricula', 'nombre', 'carrera', 'turno']