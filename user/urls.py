from django.urls import path

from user.views import *

#app_name = 'user'

urlpatterns = [
    path('lista/', User_Lista.as_view(), name="UserList"),
    path('crear/', Crear_Usuario.as_view(), name="UserCreate"),
    path('edit/<int:pk>/', Actualizar_Usuario.as_view(), name="UserUpdate"),
    path('delete/<int:pk>/', Eliminar_Usuario.as_view(), name="UserDelete"),
    path('cambio/grupo/<int:pk>/', CambioGrupoUser.as_view(), name="User_group_change"),
]
