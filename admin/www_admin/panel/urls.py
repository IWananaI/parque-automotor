from django.contrib import admin
from django.urls import path
from django import views
from . import views

urlpatterns = {
    path('',views.index, name="index"),
    path('listar',views.index, name="listar"),
    path('agregar',views.index, name="agregar"),
    path('actualizar',views.index, name="actualizar"),
    path('eliminar',views.index, name="eliminar"),

}