from django.db import models
from django.utils import timezone

class Carrera(models.Model):
    name = models.CharField(max_length=100, null=False)    
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)
    
    
    def _str_(self):
        return self.name

    class Meta:
        db_table = 'Carrera'