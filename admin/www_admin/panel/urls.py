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
    path('listarveh', views.listarveh, name="listarveh"),
    path('agregarveh', views.agregarveh, name="agregarveh"),
    path('actualizarveh/<idVehiculo>', views.actualizarveh, name="actualizarveh"),
    path('eliminarveh/<idVehiculo>', views.eliminarveh, name="eliminarveh"),
    path('listarsoa', views.listarsoa, name="listarsoa"),
    path('agregarsoa', views.agregarsoa, name="agregarsoa"),
    path('actualizarsoa/<int:idSoat>', views.actualizarsoa, name="actualizarsoa"),
    path('eliminarsoa/<int:idSoat>', views.eliminarsoa, name="eliminarsoa"),
    path('listartec', views.listartec, name="listartec"),
    path('agregartec', views.agregartec, name="agregartec"),
    path('actualizartec/<int:idTecno>', views.actualizartec, name="actualizartec"),
    path('eliminartec/<int:idTecno>', views.eliminartec, name="eliminartec"),
]