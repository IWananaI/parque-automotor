from django.contrib import admin
from django.urls import path

from django import views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('listar', views.listar, name="listar"),
    path('agregar', views.agregar, name="agregar"),
    path('actualizar/<int:idUsuario>', views.actualizar, name="actualizar"),
    path('eliminar/<int:idUsuario>', views.eliminar, name="eliminar"),
    path('listardep', views.listardep, name="listardep"),
    path('agregardep', views.agregardep, name="agregardep"),
    path('actualizardep/<int:idDependencia>', views.actualizardep, name="actualizardep"),
    path('eliminardep/<int:idDependencia>', views.eliminardep, name="eliminardep"),
]