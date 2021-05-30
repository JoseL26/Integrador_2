from django.db import models

# Create your models here.
from django.forms import model_to_dict


class Categoria(models.Model):
    Descripcion=models.CharField(max_length=40)
    Estado=models.IntegerField()

    class Meta:
        ordering = ["Descripcion"]
        verbose_name_plural="Categorias"

    def __str__(self):
        return self.Descripcion

    def toJSON(self):
        item = model_to_dict(self)
        return item

class Cargo(models.Model):
    Descripcion=models.CharField(max_length=50)
    Departament=models.CharField(max_length=40)
    Estado=models.IntegerField()

    class Meta:
        ordering = ["Descripcion"]
        verbose_name_plural="Cargos"

    def __str__(self):
        return self.Descripcion
        
    def toJSON(self):
        item = model_to_dict(self)
        return item

class Empleado(models.Model):
    Apellidos = models.CharField(max_length=40)
    Nombres = models.CharField(max_length=40)
    DNI = models.CharField(max_length=10)
    Direccion = models.CharField(max_length=45)
    Distrito = models.CharField(max_length=40)
    Provincia = models.CharField(max_length=30)
    Telefono = models.CharField(max_length=9)
    Correo = models.CharField(max_length=40)
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cargos = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    Estado = models.CharField(max_length=1)

    class Meta:
        ordering = ["Apellidos"]
        verbose_name_plural = "Empleados"

    def __str__(self):
        return '%s %s'%(self.Apellidos, self.Nombres)

    def toJSON(self):
        item = model_to_dict(self)
        return item

class CaterogiaEquipo(models.Model):
    Desc_categoria = models.CharField(max_length=40)
    Estado = models.DateField(default=1)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "CaterogiaEquipos"

    def __str__(self):
        return self.Desc_categoria

    def toJSON(self):
        item = model_to_dict(self)
        return item

class Marca(models.Model):
    Desc_marca = models.CharField(max_length=50)

    def __str__(self):
        return self.Desc_marca

class Equipo(models.Model):
    Cod_equipo = models.CharField(max_length=10, unique=True)
    Desc_equipo = models.CharField(max_length=50)
    CaterogiaEq = models.ForeignKey(CaterogiaEquipo, on_delete=models.CASCADE)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Modelo = models.CharField(max_length=30)
    Modelo_motor = models.CharField(max_length=30)
    Estado = models.IntegerField()

    def __str__(self):
        return self.Desc_equipo

class OrdenTrabajo(models.Model):
    Orden = models.CharField(max_length=10,primary_key=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    eq_sistema = models.CharField(max_length=10)
    conjunto = models.CharField(max_length=5)
    desc_conjunto = models.CharField(max_length=30)
    fase = models.CharField(max_length=4)
    Responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    estado = models.IntegerField

    def __str__(self):
        return self.equipo

class Operciones(models.Model):
    Descripcion = models.CharField(max_length=50)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    orden = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE)
    Etapa = models.CharField(max_length=10)
    Resposable = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    horas = models.DecimalField

    def __str__(self):
        return self.Descripcion

class ParteHoras(models.Model):
    Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    TotalHoras = models.DecimalField

    def __str__(self):
        return self.fecha

class DetalleParte(models.Model):
    NumParte = models.ManyToManyField(ParteHoras)
    Orden = models.ManyToManyField(OrdenTrabajo)
    operacion = models.ForeignKey(Operciones, on_delete=models.CASCADE)
    Cantidad = models.DecimalField

    def __str__(self):
        return self.NumParte



