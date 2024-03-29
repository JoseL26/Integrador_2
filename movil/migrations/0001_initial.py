# Generated by Django 3.1.6 on 2021-05-30 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=50)),
                ('Departament', models.CharField(max_length=40)),
                ('Estado', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Cargos',
                'ordering': ['Descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=40)),
                ('Estado', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Categorias',
                'ordering': ['Descripcion'],
            },
        ),
        migrations.CreateModel(
            name='CaterogiaEquipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Desc_categoria', models.CharField(max_length=40)),
                ('Estado', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name_plural': 'CaterogiaEquipos',
                'ordering': ['Desc_categoria'],
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Apellidos', models.CharField(max_length=40)),
                ('Nombres', models.CharField(max_length=40)),
                ('DNI', models.CharField(max_length=10)),
                ('Direccion', models.CharField(max_length=45)),
                ('Distrito', models.CharField(max_length=40)),
                ('Provincia', models.CharField(max_length=30)),
                ('Telefono', models.CharField(max_length=9)),
                ('Correo', models.CharField(max_length=40)),
                ('Estado', models.CharField(max_length=1)),
                ('cargos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.cargo')),
                ('categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.categoria')),
            ],
            options={
                'verbose_name_plural': 'Empleados',
                'ordering': ['Apellidos'],
            },
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cod_equipo', models.CharField(max_length=10, unique=True)),
                ('Desc_equipo', models.CharField(max_length=50)),
                ('Modelo', models.CharField(max_length=30)),
                ('Modelo_motor', models.CharField(max_length=30)),
                ('Estado', models.IntegerField()),
                ('CaterogiaEq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.caterogiaequipo')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Desc_marca', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ParteHoras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('Empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenTrabajo',
            fields=[
                ('Orden', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('eq_sistema', models.CharField(max_length=10)),
                ('conjunto', models.CharField(max_length=5)),
                ('desc_conjunto', models.CharField(max_length=30)),
                ('fase', models.CharField(max_length=4)),
                ('Responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.empleado')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Operciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=50)),
                ('Etapa', models.CharField(max_length=10)),
                ('Resposable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.empleado')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.equipo')),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.ordentrabajo')),
            ],
        ),
        migrations.AddField(
            model_name='equipo',
            name='Marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.marca'),
        ),
        migrations.CreateModel(
            name='DetalleParte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumParte', models.ManyToManyField(to='movil.ParteHoras')),
                ('Orden', models.ManyToManyField(to='movil.OrdenTrabajo')),
                ('operacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.operciones')),
            ],
        ),
    ]
