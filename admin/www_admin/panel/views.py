from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuarios
# Create your views here.

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    return render(request,"index.html")

def listar(request):
    users = Usuarios.objects.all()
    datos = { 'usuarios' : users }
    return render(request, "crud_usuarios/listar.html", datos)

def agregar(request):
    if request.method == 'POST':
        if request.POST.get('pas_per') and request.POST.get('nom_per') and request.POST.get('ape_per') and request.POST.get('tel_per') and request.POST.get('dir_per') and request.POST.get('cat_per') and request.POST.get('vig_per') and request.POST.get('dep_per'):
            
            user = Usuarios()
            user.id_per = request.POST.get('id_per')
            user.pas_per = request.POST.get('pas_per')
            user.nom_per = request.POST.get('nom_per')
            user.ape_per = request.POST.get('ape_per')
            user.tel_per = request.POST.get('tel_per')
            user.dir_per = request.POST.get('dir_per')
            user.cat_per = request.POST.get('cat_per')
            user.vig_per = request.POST.get('vig_per')
            user.dep_per = request.POST.get('dep_per')
            user.save()
            return redirect('listar')
    else:
        users = Usuarios.objects.all()
        datos = {'usuarios' : users}
        return render(request,"crud_usuarios/agregar.html",datos)

def actualizar(request):
    try:
        if request.method == 'POST':
            if request.POST.get('pas_per') and request.POST.get('nom_per') and request.POST.get('ape_per') and request.POST.get('tel_per') and request.POST.get('dir_per') and request.POST.get('cat_per') and request.POST.get('vig_per') and request.POST.get('dep_per'):
                user = Usuarios()
                user.id_per = request.POST.get('id_per')
                user.pas_per = request.POST.get('pas_per')
                user.nom_per = request.POST.get('nom_per')
                user.ape_per = request.POST.get('ape_per')
                user.tel_per = request.POST.get('tel_per')
                user.dir_per = request.POST.get('dir_per')
                user.cat_per = request.POST.get('cat_per')
                user.vig_per = request.POST.get('vig_per')
                user.dep_per = request.POST.get('dep_per')
                user.save()
                return redirect('listar')
        else:
            users = Usuarios.objects.all()
            datos = { 'usuarios' : users }
            return render(request, "crud_usuarios/actualizar.html", datos)
    except user.DoesNotExist:
        users = Usuarios.objects.all()
        datos = { 'usuarios' : users }
        return render(request, "crud_usuarios/actualizar.html", datos)


def eliminar(request):
    if request.method=='POST':
        if request.POST.get('id_per'):
            id_a_borrar= request.POST.get('id_per')
            tupla=Usuarios.objects.get(id_per = id_a_borrar)
            tupla.delete()
            return redirect('listar')
    else:
        users = Usuarios.objects.all()
        datos = { 'usuarios' : users }
        return render(request, "crud_usuarios/actualizar.html", datos)

