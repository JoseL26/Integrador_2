from django.conf.urls import url
from django.urls import path

from movil.views.cargo.views import *
from movil.views.categoria.views import *
from movil.views.empleado.views import *
app_name = 'movil'

urlpatterns = [
    url(r'^categoria/lista/$', Categori_Lista.as_view(), name="CategoriaList"),
    url(r'^categoria/lista2/$', CategoriaList, name="CategoriaList2"),
    url(r'^categoria/create/$', CategoriaCreate.as_view(), name="Categoriacreate"),
    path('categoria/edit/<int:pk>/', CategoriaUpdate.as_view(), name="Category_update"),
    url(r'^cargo/lista/$', Cargo_Lista.as_view(), name="Cargolist"),
    url(r'^cargo/create/$', CargoCreate.as_view(), name="Cargocreate"),
    path('cargo/edit/<int:pk>/', CargoUpdate.as_view(), name="Cargo_update"),
    url(r'^empleado/lista/$', Empleado_Lista.as_view(), name="ListaEmpleado"),
    url(r'^empleado/create/$', Empleado_Create.as_view(), name="Crear_Empleado"),
    path('empleado/edit/<int:pk>/', Empleado_Update.as_view(), name="Actualizar_update"),

]