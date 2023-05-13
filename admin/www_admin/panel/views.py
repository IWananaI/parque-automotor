from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    return render(request,"index.html")

def listar(request):
    return render(request,"crud_usuarios/listar.html")

def agregar(request):
    return render(request,"crud_usuarios/agregar.html")

def actualizar(request):
    return render(request,"crud_usuarios/actualizar.html")

def eliminar(request):
    return render(request,"crud_usuarios/eliminar.html")
