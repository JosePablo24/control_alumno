from django.db import models
from django.utils import timezone
from Carrera.models import Carrera

class Alumno(models.Model):
    name = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    sexo = models.CharField(max_length=100, null=False)
    matricula = models.IntegerField(null=False)
    edad = models.IntegerField(null=False)
    direccion = models.CharField(max_length=100, null=False)     
    idCarrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)
    
    def _str_(self):
        return self.name

    class Meta:
        db_table = 'Alumno'