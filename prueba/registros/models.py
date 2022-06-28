from tabnanny import verbose
from turtle import update
from django.db import models

# Create your models here.
class Alumnos(models.Model): #Define la estructura de nuestra tabla
    matricula = models.CharField(max_length=12,verbose_name="Mat")#Texto corto
    nombre = models.TextField()#Texto largo
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)#Fecha y tiempo
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]
        #el menos indica que se ordenara del mas reciente al mas viejo

    def __str__(self):
        return self.nombre
            #Indica que se mostrara el nombre como valor en la tabla