from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Carrera.models import Carrera
from Carrera.serializer import CarreraSerializers

class CarreraList(APIView):
    def post(self, request, format=None):
        serializer = CarreraSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get(self, request, format = None):
        queryset = Carrera.objects.filter(delete = False)
        serializer = CarreraSerializers(queryset, many = True) 
        return Response(serializer.data)

class CarreraDelete(APIView):
    def get_object(self, id):        
        try:
            return Carrera.objects.get(pk = id) 
        except Carrera.DoesNotExist:            
            return 404
            
    def delete(self, request, id, format = None):
        carrera = self.get_object(id)          
        if carrera != 404:
            Carrera.objects.filter(id=id).delete() 
            return Response('hecho')

class CarreraDetail(APIView):
    def get_object(self, id):        
        try:
            return Carrera.objects.get(pk = id) 
        except Carrera.DoesNotExist:            
            return 404

    def get(self, id, request, format = None):
        carrera = self.get_object(id = id)
        if carrera != 404:
            serializer = CarreraSerializers(carrera) 
            return Response(serializer.data)            
        else:
            return Response(Carrera)            

    def put(self, id, request, format = None):
        carrera = self.get_object(id = id)
        if carrera != 404:
            serializer = CarreraSerializers(carrera, data = request.data) 
            if serializer.is_valid():
                serializer.save()
                data = serializer.data()                
                return Response(data)            
        else:
            return Response(carrera, status = status.HTTP_400_BAD_REQUEST)