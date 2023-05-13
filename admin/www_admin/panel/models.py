from django.db import models

# Create your models here.

class Usuarios(models.Model):
    id_per = models.IntegerField(primary_key=True)
    pas_per = models.CharField(max_length=30,null=False)
    nom_per = models.CharField(max_length=30,null=False)
    ape_per = models.CharField(max_length=30,null=False)
    tel_per = models.IntegerField(null=False)
    dir_per = models.CharField(max_length=30,null=False)
    cat_per = models.CharField(max_length=2,null=False)
    vig_per = models.DateField(null=True)
    dep_per = models.IntegerField(null=False)
    class Meta:
        db_table = 'usuarios'
