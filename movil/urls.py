from django.conf.urls import url
from django.urls import path

from movil.views.actividades.views import Parte_horas_create
from movil.views.cargo.views import *
from movil.views.categoria.views import *
from movil.views.categoria_equipo.views import *
from movil.views.dashboard.views import DashboardView
from movil.views.empleado.views import *
from movil.views.equipo.views import *
from movil.views.listas.views import TestView
from movil.views.marca.views import *
from movil.views.orden_trabajo.views import *
from movil.views.usuario.views import *
from movil.views.parte_horas.views import *
from movil.views.det_phoras.views import *

app_name = 'movil'

urlpatterns = [
    url(r'^categoria/lista/$', Categori_Lista.as_view(), name="CategoriaList"),
    url(r'^categoria/create/$', CategoriaCreate.as_view(), name="Categoriacreate"),
    url(r'^categoria/form/$', CategoriaFormView.as_view(), name="Categoriaform"),
    path('categoria/edit/<int:pk>/', CategoriaUpdate.as_view(), name="Category_update"),
    path('categoria/delete/<int:pk>/', CategoriaDelete.as_view(), name="Category_delete"),
    url(r'^cargo/lista/$', Cargo_Lista.as_view(), name="Cargolist"),
    url(r'^cargo/create/$', CargoCreate.as_view(), name="Cargocreate"),
    path('cargo/edit/<int:pk>/', CargoUpdate.as_view(), name="Cargo_update"),
    url(r'^empleado/lista/$', Empleado_Lista.as_view(), name="ListaEmpleado"),
    url(r'^empleado/create/$', Empleado_Create.as_view(), name="Crear_Empleado"),
    path('empleado/edit/<int:pk>/', Empleado_Update.as_view(), name="Actualizar_update"),
    url(r'^cat_equipo/lista/$', Categori_Lista_Equipo.as_view(), name="CategoriaListEq"),
    url(r'^cat_equipo/create/$', CategoriaCreateEq.as_view(), name="CategoraCreatet_Eq"),
    path('cat_equipo/edit/<int:pk>/', CategoriaUpdateEq.as_view(), name="Categoriaupdate_Eq"),
    url(r'^marca/lista/$', Marca_Lista_Equipo.as_view(), name="MarcaListEq"),
    url(r'^marca/create/$', MarcaCreateEq.as_view(), name="MarcaCreate_Eq"),
    path('marca/edit/<int:pk>/', MarcaUpdateEq.as_view(), name="Marcaupdate_Eq"),
    url(r'^equipo/lista/$', Lista_Equipo.as_view(), name="Lista_Equipo"),
    url(r'^equipo/create/$', Create_Equipo.as_view(), name="Create_Equipo"),
    path('equipo/edit/<int:pk>/', Update_Equipo.as_view(), name="Update_Equipo"),
    url(r'^orden_trabajo/lista/$', Orden_Lista.as_view(), name="OrdenList"),
    url(r'^orden_trabajo/create/$', OrdenCreate.as_view(), name="OrdenCreate"),
    path('orden_trabajo/edit/<int:pk>/', OrdenUpdate.as_view(), name="update_orden"),

    url(r'^parte_horas/lista/$', Phoras_Lista.as_view(), name="PhorasList"),
    url(r'^parte_horas/create/$', Phoras_Create.as_view(), name="PhorasCreate"),
    path('parte_horas/edit/<int:pk>/', Phoras_Update.as_view(), name="PhorasUpdate"),

    url(r'^detparte_horas/lista/$', DetPhoras_Lista.as_view(), name="DetPhorasList"),
    url(r'^detparte_horas/create/$', DetPhoras_Create.as_view(), name="DetPhorasCreate"),
    path('detparte_horas/edit/<int:pk>/', DetPhoras_Update.as_view(), name="DetPhorasUpdate"),

    url(r'^actividades/create/$', Parte_horas_create.as_view(), name="ParteCreate"),

    #pagina de principal
    url(r'^dashboard/$', DashboardView.as_view(), name="Dashboard"),
    #listados
    url(r'^listas/$', TestView.as_view(), name="test"),

    url(r'^usuario/lista/$', Usuario_Lista.as_view(), name="UsuarioList"),
    url(r'^usuario/create/$', UsuarioCreate.as_view(), name="UsuarioCreate"),
    path('usuario/edit/<int:pk>/', UsuarioUpdate.as_view(), name="Usuario_Update"),
    #url(r'^usuario/login/$', name="UsuarioList"),

]