# Generated by Django 3.1.6 on 2021-06-19 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movil', '0011_auto_20210619_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetParte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo', models.CharField(blank=True, max_length=45, null=True)),
                ('operacion', models.IntegerField(blank=True, default=0, null=True)),
                ('desc_actividad', models.CharField(blank=True, max_length=100)),
                ('Cantidad', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('Orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.ordentrabajo')),
                ('parte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.partehoras')),
            ],
            options={
                'verbose_name_plural': 'DetallePartes',
                'ordering': ['operacion'],
            },
        ),
        migrations.RemoveField(
            model_name='operciones',
            name='Etapa',
        ),
        migrations.RemoveField(
            model_name='operciones',
            name='Resposable',
        ),
        migrations.RemoveField(
            model_name='operciones',
            name='equipo',
        ),
        migrations.DeleteModel(
            name='DetalleParte',
        ),
    ]
