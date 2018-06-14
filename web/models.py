from django.db import models
from datetime import date
# Create your models here.


class Course(models.Model):
    nombre = models.CharField(max_length=30)
    fecha = models.DateField()
    tema = models.CharField(max_length=30)
    lugar = models.CharField(max_length=30)
    info = models.TextField()
    activo = models.BooleanField(default=True)

    def complete(self):
        complete_name = "{0}  ({1})"
        return complete_name.format(self.nombre, self.fecha)

    def __str__(self):
        return self.complete()


class Assistant(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    telefono = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    area_de_trabajo = models.CharField(max_length=40)
    lugar_de_trabajo = models.CharField(max_length=40)

    def complete(self):
        complete_name = "{0} , {1}"
        return complete_name.format(self.apellidos, self.nombres)

    def __str__(self):
        return self.complete()


class Inscription(models.Model):
    asistente = models.ForeignKey(Assistant, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    def complete(self):
        complete_name = "{0} ==> {1}"
        return complete_name.format(self.asistente, self.curso)

    def __str__(self):
        return self.complete()


class Message(models.Model):
    nombre = models.CharField(max_length=35)
    email = models.EmailField()
    mensaje = models.TextField()
    date = models.DateField(default=date.today)
