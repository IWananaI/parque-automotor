from django.db import models

# Create your models here.

class Dependencias(models.Model):
    id_dep = models.AutoField(primary_key=True)
    nom_dep = models.CharField(max_length=50,null=False)
    class Meta:
        db_table = 'dependencias'

class Usuarios(models.Model):
    id_per = models.BigIntegerField(primary_key=True)
    pas_per = models.CharField(max_length=30,null=False)
    nom_per = models.CharField(max_length=30,null=False)
    ape_per = models.CharField(max_length=30,null=False)
    tel_per = models.CharField(max_length=30,null=False)
    dir_per = models.CharField(max_length=30,null=False)
    cat_per = models.CharField(max_length=2,null=False)
    vig_per = models.DateField(null=True)
    dep_per = models.ForeignKey(Dependencias, on_delete=models.CASCADE)
    class Meta:
        db_table = 'usuarios'


class Soat(models.Model):
    id_soa = models.IntegerField(primary_key=True)
    nom_emp_soa = models.CharField(max_length=50, null=False)
    fec_exp_soa = models.DateField(null=True)
    fec_ven_soa = models.DateField(null=True)
    class Meta:
        db_table = 'soat'

class Tecnicomecanica(models.Model):
    id_tec = models.IntegerField(primary_key=True)
    nom_emp_tec = models.CharField(max_length=50, null=False)
    fec_exp_tec = models.DateField(null=True)
    fec_ven_tec = models.DateField(null=True)
    class Meta:
        db_table = 'tecnicomecanica'


class Vehiculos(models.Model):
    pla_veh = models.CharField(max_length=10,primary_key=True)
    num_lic_veh = models.BigIntegerField(null=False)
    cla_veh = models.CharField(max_length=50,null=False)
    mar_veh = models.CharField(max_length=50,null=False)
    mod_veh = models.IntegerField(null=False)
    col_veh = models.CharField(max_length=30,null=False)
    num_mot_veh = models.CharField(max_length=50,null=False)
    num_cha_veh = models.CharField(max_length=50,null=False)
    cil_veh = models.IntegerField(null=False)
    tip_car_veh = models.CharField(max_length=50,null=False)
    est_veh = models.BooleanField(null=False)
    obs_veh = models.CharField(max_length=200,null=False)
    dep_veh = models.ForeignKey(Dependencias,
                                on_delete=models.CASCADE,
                                blank=True)
    per_asi_veh = models.ManyToManyField(Usuarios,
                                        through='VehiculosAsignados',
                                        blank=True)
    soa_veh = models.ForeignKey(Soat,
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE)
    tec_veh = models.ForeignKey(Tecnicomecanica,
                                null=True,
                                blank=True,
                                on_delete=models.CASCADE)
    class Meta:
        db_table = 'vehiculos'

class VehiculosAsignados(models.Model):
    id_per = models.ForeignKey(Usuarios,
                               blank=True,
                               on_delete=models.CASCADE)
    id_veh = models.ForeignKey(Vehiculos,
                               blank=True,
                               on_delete=models.CASCADE)
    fec_ing = models.DateTimeField(null=False)
    fec_sal = models.DateTimeField(null=True)
    obs_veh_asi = models.CharField(max_length=200)
    class Meta:
        db_table = 'vehiculos_asignados'
