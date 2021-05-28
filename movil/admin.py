from django.contrib import admin
from movil.models import Categoria,Cargo, Empleado
# Register your models here.
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id','Descripcion','Departament','Estado')

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id','Apellidos','Nombres','DNI','Direccion','Distrito','Provincia','Telefono',
                    'Correo', 'categorias','cargos','Estado')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id','Descripcion','Estado')


admin.site.register(Cargo, CargoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Empleado, EmpleadoAdmin)