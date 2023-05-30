from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuarios, Dependencias, Vehiculos, Soat, Tecnicomecanica
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
            user.dep_per_id = request.POST.get('dep_per')
            user.save()
            return redirect('listar')
    else:
        users = Usuarios.objects.all()
        deps = Dependencias.objects.all()
        datos = {'usuarios' : users, 'dependencias': deps}
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
            user = Usuarios.objects.get( id_per=idUsuario )
            datos = { 'usuarios' : users , 'usuario' : user }
            return render(request, "crud_usuarios/actualizar.html", datos)
    except Usuarios.DoesNotExist:
        users = Usuarios.objects.all()
        user = None
        datos = { 'usuarios' : users , 'usuario' : user }
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

def listardep(request):

    if request.method == 'POST':
        busqueda = request.POST.get('keyword')
        lista = Dependencias.objects.all()

        if busqueda is not None:
            res_busqueda = lista.filter(
            Q(id_dep__icontains=busqueda) |
            Q(nom_dep__icontains=busqueda) 
            )
            datos = {'dependencias': res_busqueda}
            return render(request, "crud_dependencias/listar.html", datos)
        else:
            datos = { 'dependencias' : lista }
            return render(request, "crud_dependencias/listar.html", datos)
    else:
        deps = Dependencias.objects.order_by('-id_dep')[:10]
        datos = { 'dependencias' : deps }
        return render(request, "crud_dependencias/listar.html", datos)

def agregardep(request):
    if request.method == 'POST':
        if request.POST.get('nom_dep'):
            
            dep = Dependencias()
            dep.nom_dep = request.POST.get('nom_dep')
            dep.save()
            return redirect('listardep')
    else:
        deps = Dependencias.objects.all()
        datos = {'dependencias' : deps}
        return render(request,"crud_dependencias/agregar.html",datos)

def actualizardep(request, idDependencia):
    try:
        if request.method == 'POST':
            if request.POST.get('nom_dep'):
                dep = Dependencias()
                dep.id_dep = request.POST.get('id')
                dep.nom_dep = request.POST.get('nom_dep')
                dep.save()
                return redirect('listardep')
        else:
            deps = Dependencias.objects.all()
            dep = Dependencias.objects.get( id_dep=idDependencia )
            datos = { 'dependencias' : deps , 'dependencia' : dep }
            return render(request, "crud_dependencias/actualizar.html", datos)
    except Dependencias.DoesNotExist:
        deps = Dependencias.objects.all()
        dep = None
        datos = { 'dependencias' : deps , 'dependencia' : dep }
        return render(request, "crud_dependencias/actualizar.html", datos)


def eliminardep(request, idDependencia):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar= request.POST.get('id')
                tupla=Dependencias.objects.get(id_dep = id_a_borrar)
                tupla.delete()
                return redirect('listardep')
        else:
            deps = Dependencias.objects.all()
            dep = Dependencias.objects.get( id_dep=idDependencia )
            datos = { 'dependencias' : deps , 'dependencia' : dep }
            return render(request, "crud_dependencias/eliminar.html", datos)
    except Dependencias.DoesNotExist:
        deps = Dependencias.objects.all()
        dep = None
        datos = { 'dependencias' : deps , 'dependencia' : dep }
        return render(request, "crud_dependencias/eliminar.html", datos)    
    
def listarveh(request):

    if request.method == 'POST':
        busqueda = request.POST.get('keyword')
        lista = Vehiculos.objects.all()

        if busqueda is not None:
            res_busqueda = lista.filter(
            Q(pla_veh__icontains=busqueda) |
            Q(num_lic_veh__icontains=busqueda) |
            Q(cla_veh__icontains=busqueda) |
            Q(mar_veh__icontains=busqueda) |
            Q(mod_veh__icontains=busqueda) |
            Q(col_veh__icontains=busqueda) |
            Q(num_mot_veh__icontains=busqueda) |
            Q(num_cha_veh__icontains=busqueda) |
            Q(cil_veh__icontains=busqueda) |
            Q(tip_car_veh__icontains=busqueda) |
            Q(est_veh__icontains=busqueda) |
            Q(obs_veh__icontains=busqueda) |
            Q(dep_veh__icontains=busqueda) |
            Q(per_asi_veh__icontains=busqueda) |
            Q(soa_veh__icontains=busqueda) |
            Q(tec_veh__icontains=busqueda) 
            )
            datos = {'vehiculos': res_busqueda}
            return render(request, "crud_vehiculos/listar.html", datos)
        else:
            datos = { 'vehiculos' : lista }
            return render(request, "crud_vehiculos/listar.html", datos)
    else:
        deps = Dependencias.objects.order_by('-id_dep')[:10]
        datos = { 'vehiculos' : deps }
        return render(request, "crud_vehiculos/listar.html", datos)
def agregarveh(request):
    if request.method == 'POST':
        if request.POST.get('num_lic_veh') and request.POST.get('num_lic_veh') and request.POST.get('cla_veh') and request.POST.get('mar_veh') and request.POST.get('mod_veh') and request.POST.get('col_veh') and request.POST.get('num_mot_veh') and request.POST.get('num_cha_veh') and request.POST.get('cil_veh') and request.POST.get('tip_car_veh') and request.POST.get('est_veh') and request.POST.get('obs_veh') :
            print("Hola mundo, si entro")
            veh = Vehiculos()
            veh.pla_veh = request.POST.get('pla_veh')
            veh.num_lic_veh = request.POST.get('num_lic_veh')
            veh.cla_veh = request.POST.get('cla_veh')
            veh.mar_veh = request.POST.get('mar_veh')
            veh.mod_veh = request.POST.get('mod_veh')
            veh.col_veh = request.POST.get('col_veh')
            veh.num_mot_veh = request.POST.get('num_mot_veh')
            veh.num_cha_veh = request.POST.get('num_cha_veh')
            veh.cil_veh = request.POST.get('cil_veh')
            veh.tip_car_veh = request.POST.get('tip_car_veh')
            veh.est_veh = request.POST.get('est_veh')
            veh.obs_veh = request.POST.get('obs_veh')
            veh.dep_veh_id = request.POST.get('dep_veh')
            veh.soa_veh_id = request.POST.get('soa_veh')
            veh.tec_veh_id = request.POST.get('tec_veh')
            veh.save()
            return redirect('listarveh')
    else:
        vehs = Vehiculos.objects.all()
        deps = Dependencias.objects.all()
        soats = Soat.objects.all()
        tecs = Tecnicomecanica.objects.all()
        
        datos = {'vehiculos' : vehs, 'dependencias' : deps,'soats': soats, 'tecnos': tecs}
        return render(request,"crud_vehiculos/agregar.html",datos)