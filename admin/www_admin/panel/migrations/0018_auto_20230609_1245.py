# Generated by Django 3.1.7 on 2023-06-09 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0017_auto_20230601_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculosasignados',
            name='fec_ing',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
