from __future__ import unicode_literals

from django.db import models
from modulos.adopcion.models import Persona

# Create your models here.

class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return '{}'.format(self.nombre)

class Mascota(models.Model):
    image = models.ImageField(upload_to='mascotas', null=True, blank=True,)
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10, null=True, blank=True,)
    edad_aproximada = models.IntegerField(null=True, blank=True,)
    fecha_rescate = models.DateField(null=True, blank=True,)
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna, blank=True)