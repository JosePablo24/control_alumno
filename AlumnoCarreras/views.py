from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from AlumnoCarreras.models import AlumnoCarreras
from AlumnoCarreras.serializer import AlumnoCarrerasSerializers

class AlumnoCarrerasList(APIView):
    def get(self, request, format=None):
        queryset = AlumnoCarreras.objects.filter(delete=False)
        serializer = AlumnoCarrerasSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlumnoCarrerasSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlumnoCarrerasDetail(APIView):
    def get_object(self, id):
        try:
            return AlumnoCarreras.objects.get(pk=id) 
        except AlumnoCarreras.DoesNotExist:
            return 404

    def get(self, request, id, format=None):
        alumno = self.get_object(id)
        if alumno != 404:
            serializer = AlumnoCarrerasSerializers(alumno)
            return Response(serializer.data)
        else:
            return Response(alumno)

    def put(self, request, id, format=None):
        alumno = self.get_object(id)
        if alumno != 404:
            serializer = AlumnoCarrerasSerializers(alumno, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(alumno, status = status.HTTP_400_BAD_REQUEST)

class AlumnoCarrerasDelete(APIView):
    def get_object(self, id):        
        try:
            return AlumnoCarreras.objects.get(pk = id) 
        except AlumnoCarreras.DoesNotExist:            
            return 404
            
    def delete(self, request, id, format = None):
        alumno = self.get_object(id)          
        if alumno != 404:
            AlumnoCarreras.objects.filter(id=id).delete() 
            return Response('hecho')