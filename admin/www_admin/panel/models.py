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
    fec_exp_soa = models.DateField(null=True)
    fec_ven_soa = models.DateField(null=True)
    class Meta:
        db_table = 'soat'

class Tecnicomecanica(models.Model):
    id_tec = models.IntegerField(primary_key=True)
    fec_exp_tec = models.DateField(null=True)
    fec_ven_tec = models.DateField(null=True)
    class Meta:
        db_table = 'tecnicomecanica'

