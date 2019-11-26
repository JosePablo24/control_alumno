from rest_framework import routers, serializers, viewsets

from AlumnoCarreras.models import AlumnoCarreras

class AlumnoCarrerasSerializers(serializers.ModelSerializer):
    class Meta:
        model = AlumnoCarreras
        fields = ('__all__')