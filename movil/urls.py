from django.conf.urls import url
from django.urls import path

from movil.views.actividades.views import *
from movil.views.cargo.views import *
from movil.views.categoria.views import *
from movil.views.categoria_equipo.views import *
from movil.views.dashboard.views import DashboardView
from movil.views.empleado.views import *
from movil.views.equipo.views import *
from movil.views.listas.views import TestView
from movil.views.marca.views import *
from movil.views.orden_trabajo.views import *


app_name = 'movil'

urlpatterns = [
    #vistas de categoria
    url(r'^categoria/lista/$', Categori_Lista.as_view(), name="CategoriaList"),
    url(r'^categoria/create/$', CategoriaCreate.as_view(), name="Categoriacreate"),
    url(r'^categoria/form/$', CategoriaFormView.as_view(), name="Categoriaform"),
    path('categoria/edit/<int:pk>/', CategoriaUpdate.as_view(), name="Category_update"),
    path('categoria/delete/<int:pk>/', CategoriaDelete.as_view(), name="Category_delete"),

    #vistas de cargo
    url(r'^cargo/lista/$', Cargo_Lista.as_view(), name="Cargolist"),
    url(r'^cargo/create/$', CargoCreate.as_view(), name="Cargocreate"),
    path('cargo/edit/<int:pk>/', CargoUpdate.as_view(), name="Cargo_update"),

    #Vistas de empleado
    url(r'^empleado/lista/$', Empleado_Lista.as_view(), name="ListaEmpleado"),
    url(r'^empleado/create/$', Empleado_Create.as_view(), name="Crear_Empleado"),
    path('empleado/edit/<int:pk>/', Empleado_Update.as_view(), name="Actualizar_update"),

    #Vistas de categoria de equipo
    url(r'^cat_equipo/lista/$', Categori_Lista_Equipo.as_view(), name="CategoriaListEq"),
    url(r'^cat_equipo/create/$', CategoriaCreateEq.as_view(), name="CategoraCreatet_Eq"),
    path('cat_equipo/edit/<int:pk>/', CategoriaUpdateEq.as_view(), name="Categoriaupdate_Eq"),

    #Vistas de marca
    url(r'^marca/lista/$', Marca_Lista_Equipo.as_view(), name="MarcaListEq"),
    url(r'^marca/create/$', MarcaCreateEq.as_view(), name="MarcaCreate_Eq"),
    path('marca/edit/<int:pk>/', MarcaUpdateEq.as_view(), name="Marcaupdate_Eq"),

    #Vistas de equipo
    url(r'^equipo/lista/$', Lista_Equipo.as_view(), name="Lista_Equipo"),
    url(r'^equipo/create/$', Create_Equipo.as_view(), name="Create_Equipo"),
    path('equipo/edit/<int:pk>/', Update_Equipo.as_view(), name="Update_Equipo"),

    #Vistas de orden de trabajo
    url(r'^orden_trabajo/lista/$', Orden_Lista.as_view(), name="OrdenList"),
    url(r'^orden_trabajo/create/$', OrdenCreate.as_view(), name="OrdenCreate"),
    path('orden_trabajo/edit/<int:pk>/', OrdenUpdate.as_view(), name="update_orden"),

    #parte de horas
    url(r'^actividades/lista/$', Parte_horas_list.as_view(), name="PhorasList"),
    url(r'^actividades/create/$', Parte_horas_create.as_view(), name="ParteCreate"),
    path('actividades/delete/<int:pk>/', Parte_horas_delete.as_view(), name="Partedelete"),
    path('actividades/edit/<int:pk>/', Parte_horas_update.as_view(), name="Parteupdate"),
    path('actividades/imprimir/pdf/<int:pk>/', generarPDF_parte.as_view(), name="Pdfgenerate"),

    #pagina de principal
    url(r'^dashboard/$', DashboardView.as_view(), name="Dashboard"),
    #listados
    url(r'^listas/$', TestView.as_view(), name="test"),
]