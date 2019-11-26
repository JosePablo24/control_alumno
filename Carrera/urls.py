from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from Carrera import views

urlpatterns = [
    re_path(r'carrera_List/$', views.CarreraList.as_view()),
    re_path(r'alumno_detail/(?P<id>\d+)$', views.CarreraDetail.as_view()),
    re_path(r'carrera_Delete/(?P<id>\d+)$', views.CarreraDelete.as_view()),
]
