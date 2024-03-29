# Generated by Django 3.1.6 on 2021-06-16 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movil', '0006_auto_20210605_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='Descripcion',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='Descripcion',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='caterogiaequipo',
            name='Desc_categoria',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='Correo',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='DNI',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='Desc_equipo',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='marca',
            name='Desc_marca',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
