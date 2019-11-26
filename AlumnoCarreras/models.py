from django.db import models
from django.utils import timezone
from Alumno.models import Alumno
from Carrera.models import Carrera

class AlumnoCarreras(models.Model):
    idAlumno= models.ForeignKey(Alumno,on_delete=models.CASCADE)    
    idCarrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)    
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)
    
    def _str_(self):
        return self.name

    class Meta:
        db_table = 'AlumnoCarreras'