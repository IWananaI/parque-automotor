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
    cat_per = models.CharField(max_length=30,null=False)
    vig_per = models.DateField(null=True)
    dep_per = models.ForeignKey(Dependencias, on_delete=models.CASCADE)
    class Meta:
        db_table = 'usuarios'


class Soat(models.Model):
    id_soa = models.AutoField(primary_key=True)
    nom_emp_soa = models.CharField(max_length=50, null=True)
    fec_exp_soa = models.DateField(null=True)
    fec_ven_soa = models.DateField(null=True)
    class Meta:
        db_table = 'soat'

class Tecnicomecanica(models.Model):
    id_tec = models.AutoField(primary_key=True)
    nom_emp_tec = models.CharField(max_length=50, null=True)
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
    obs_veh = models.CharField(max_length=200,null=True)
    dep_veh = models.ForeignKey(Dependencias,
                                on_delete=models.CASCADE,
                                blank=True,
                                null = True)
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
    fec_ing = models.DateTimeField(auto_now_add=True ,null=True)
    fec_sal = models.DateTimeField(null=True)
    obs_veh_asi = models.CharField(max_length=200)
    class Meta:
        db_table = 'vehiculos_asignados'

class Preoperacionalesm(models.Model):
    id_pre = models.AutoField(primary_key=True)
    niv_pre = models.CharField(max_length=20,null=False)
    man_pre = models.CharField(max_length=20,null=False)
    dir_pre = models.CharField(max_length=20,null=False)
    gua_pre = models.CharField(max_length=20,null=False)
    cha_pre = models.CharField(max_length=20,null=False)
    sus_pre = models.CharField(max_length=20,null=False)
    fre_pre = models.CharField(max_length=20,null=False)
    lla_pre = models.CharField(max_length=20,null=False)
    rin_pre = models.CharField(max_length=20,null=False)
    tre_pre = models.CharField(max_length=20,null=False)
    exo_pre = models.CharField(max_length=20,null=False)
    ret_pre = models.CharField(max_length=20,null=False)
    man_mec_pre = models.CharField(max_length=20,null=False)
    luc_pre = models.CharField(max_length=20,null=False)
    dir_stop_pre = models.CharField(max_length=20,null=False)
    pit_pre = models.CharField(max_length=20,null=False)
    obs_pre = models.CharField(max_length=300)
    fec_pre = models.DateTimeField(null=True),
    pla_pre = models.ForeignKey(Vehiculos,
                                on_delete=models.CASCADE,
                                blank=True,
                                null = True)
    
    class Meta:
        db_table = 'preoperacionalesm'