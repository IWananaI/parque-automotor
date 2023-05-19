from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuarios
from django.db.models import Q
# Create your views here.

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    return render(request,"index.html")

def listar(request):

    if request.method == 'POST':
        busqueda = request.POST.get('keyword')
        lista = Usuarios.objects.all()

        if busqueda is not None:
            res_busqueda = lista.filter(
            Q(id_per__icontains=busqueda) |
            Q(nom_per__icontains=busqueda) |
            Q(ape_per__icontains=busqueda) |
            Q(tel_per__icontains=busqueda) |
            Q(dir_per__icontains=busqueda) |
            Q(cat_per__icontains=busqueda) |
            Q(vig_per__icontains=busqueda) |
            Q(dep_per__icontains=busqueda) 
            )
            datos = {'usuarios': res_busqueda}
            return render(request, "crud_usuarios/listar.html", datos)
        else:
            datos = { 'usuarios' : lista }
            return render(request, "crud_usuarios/listar.html", datos)
    else:
        users = Usuarios.objects.order_by('-id_per')[:10]
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

def actualizar(request, idUsuario):
    try:
        if request.method == 'POST':
            if request.POST.get('pas_per') and request.POST.get('nom_per') and request.POST.get('ape_per') and request.POST.get('tel_per') and request.POST.get('dir_per') and request.POST.get('cat_per') and request.POST.get('vig_per') and request.POST.get('dep_per'):
                user = Usuarios()
                user.id_per = request.POST.get('id')
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
            user = Usuarios.objects.get(id_per=idUsuario)
            datos = { 'usuarios' : users , 'usuario' : user}
            return render(request, "crud_usuarios/actualizar.html", datos)
    except Usuarios.DoesNotExist:
        users = Usuarios.objects.all()
        user = None
        datos = { 'usuarios' : users , 'usuario' : user}
        return render(request, "crud_usuarios/actualizar.html", datos)


def eliminar(request, idUsuario):
    try:
        if request.method=='POST':
            if request.POST.get('id_per'):
                id_a_borrar= request.POST.get('id_per')
                tupla=Usuarios.objects.get(id_per = id_a_borrar)
                tupla.delete()
                return redirect('listar')
        else:
            users = Usuarios.objects.all()
            user = Usuarios.objects.get(id_per=idUsuario)
            datos = { 'usuarios' : users , 'usuario' : user}
            return render(request, "crud_usuarios/eliminar.html", datos)
    except Usuarios.DoesNotExist:
        users = Usuarios.objects.all()
        user = None
        datos = { 'usuarios' : users , 'usuario' : user}
        return render(request, "crud_usuarios/eliminar.html", datos)
