from rest_framework import routers, serializers, viewsets

from Carrera.models import Carrera

class CarreraSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = ('__all__')