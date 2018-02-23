from django.db import models
from datetime import date
# Create your models here.


class Assistant(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    date = models.DateField(default=date.today)

    def complete(self):
        complete_name = "{0} , {1}"
        return complete_name.format(self.apellidos, self.nombres)

    def __str__(self):
        return self.complete()


class Message(models.Model):
    nombre = models.CharField(max_length=35)
    email = models.EmailField()
    mensaje = models.TextField()
    date = models.DateField(default=date.today)
