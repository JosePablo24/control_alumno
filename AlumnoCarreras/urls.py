from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from AlumnoCarreras import views
 
urlpatterns = [
    re_path(r'alumnoCarreras_lista/$', views.AlumnoCarrerasList.as_view()),
    re_path(r'alumnoCarreras_detail/(?P<id>\d+)$', views.AlumnoCarrerasDetail.as_view()),
    re_path(r'alumnoCarreras_Delete/(?P<id>\d+)$', views.AlumnoCarrerasDelete.as_view()),
]