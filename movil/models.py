from crum import get_current_user
from django.db import models

from datetime import datetime

# Create your models here.
from django.forms import model_to_dict

from lista.models import BaseModelo


class Categoria(BaseModelo):
    Descripcion = models.CharField(max_length=40, unique=True)
    Estado = models.IntegerField(default=1)

    class Meta:
        ordering = ["Descripcion"]
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.Descripcion

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario_autor = user
            else:
                self.usuario_modificador = user
        super(Categoria, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

class Cargo(models.Model):
    Descripcion = models.CharField(max_length=50, unique=True)
    Departament = models.CharField(max_length=40)
    Estado = models.IntegerField(default=1)

    class Meta:
        ordering = ["Descripcion"]
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.Descripcion
        
    def toJSON(self):
        item = model_to_dict(self)
        return item

class Empleado(models.Model):
    Apellidos = models.CharField(max_length=40)
    Nombres = models.CharField(max_length=40)
    DNI = models.CharField(max_length=10, unique=True)
    Direccion = models.CharField(max_length=45)
    Distrito = models.CharField(max_length=40)
    Provincia = models.CharField(max_length=30)
    Telefono = models.CharField(max_length=9)
    Correo = models.CharField(max_length=40, unique=True)
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cargos = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    Estado = models.IntegerField(default=1)

    class Meta:
        ordering = ["Apellidos"]
        verbose_name_plural = "Empleados"

    def __str__(self):
        return '%s %s'%(self.Apellidos, self.Nombres)

    def toJSON(self):
        item = model_to_dict(self)
        return item

class Usuario(models.Model):
    Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    Usuario = models.CharField(max_length=30)
    Clave = models.CharField(max_length=30)

    class Meta:
        ordering = ["Usuario"]
        verbose_name_plural="Usuarios"

    def __str__(self):
        return self.Usuario
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

class CaterogiaEquipo(models.Model):
    Desc_categoria = models.CharField(max_length=40, unique=True)
    Estado = models.IntegerField(default=1)

    class Meta:
        ordering = ["Desc_categoria"]
        verbose_name_plural = "CaterogiaEquipos"

    def __str__(self):
        return self.Desc_categoria

    def toJSON(self):
        item = model_to_dict(self)
        return item

class Marca(models.Model):
    Desc_marca = models.CharField(max_length=50, unique=True)
    Estado = models.IntegerField(default=1)

    class Meta:
        ordering = ["Desc_marca"]
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.Desc_marca

    def toJSON(self):
        item = model_to_dict(self)
        return item

class Equipo(models.Model):
    Cod_equipo = models.CharField(max_length=10, unique=True)
    Desc_equipo = models.CharField(max_length=50, unique=True)
    CaterogiaEq = models.ForeignKey(CaterogiaEquipo, on_delete=models.CASCADE)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Modelo = models.CharField(max_length=30)
    Modelo_motor = models.CharField(max_length=30)
    Estado = models.IntegerField(default=1)

    class Meta:
        ordering = ["Desc_equipo"]
        verbose_name_plural = "Equipos"

    def __str__(self):
        return self.Cod_equipo

    def toJSON(self):
        item = model_to_dict(self)
        item['CaterogiaEq'] = self.CaterogiaEq.toJSON()
        item['Marca'] = self.Marca.toJSON()
        return item



class OrdenTrabajo(models.Model):
    Orden = models.CharField(max_length=10, primary_key=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    eq_sistema = models.CharField(max_length=10)
    conjunto = models.CharField(max_length=5)
    desc_conjunto = models.CharField(max_length=30)
    fase = models.CharField(max_length=4)
    Responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    estado = models.IntegerField(default=1)

    class Meta:
        ordering = ["Orden"]
        verbose_name_plural = "Ordenes"

    def __str__(self):
        return self.Orden

    def toJSON(self):
        item = model_to_dict(self)
        item['equipo'] = self.equipo.toJSON()
        item['Responsable'] = self.Responsable.toJSON()
        return item

class Operciones(models.Model):
    Descripcion = models.CharField(max_length=50)
    orden = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE)
    horas = models.DecimalField(default=00.00, max_digits=4, decimal_places=2)

    def __str__(self):
        return self.Descripcion

class ParteHoras(models.Model):
    Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.now)
    TotalHoras = models.DecimalField(default=00.00, max_digits=4, decimal_places=2)

    class Meta:
        ordering = ["id"]
        verbose_name = "ParteHora"
        verbose_name_plural = "ParteHoras"

    def __str__(self):
        return self.Empleado.Nombres

    def toJSON(self):
        item = model_to_dict(self)
        item['Empleado'] = self.Empleado.toJSON()
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        item['TotalHoras'] = format(self.TotalHoras, '.2f')
        item['det'] = [i.toJSON() for i in self.detparte_set.all()]
        return item


class DetParte(models.Model):
    parte = models.ForeignKey(ParteHoras, on_delete=models.CASCADE)
    Orden = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE)
    operacion = models.IntegerField(default=0, blank=True, null=True)
    desc_actividad = models.CharField(max_length=100, blank=True)
    Cantidad = models.DecimalField(default=00.00, max_digits=4, decimal_places=2)

    class Meta:
        ordering = ["id"]
        verbose_name = "Detalle de parte"
        verbose_name_plural = "Detalle de partes"

    def __str__(self):
        return self.Orden.Orden

    def toJSON(self):
        item = model_to_dict(self, exclude=['parte'])
        item['Orden'] = self.Orden.toJSON()
        item['Cantidad'] = format(self.Cantidad, '.2f')
        return item