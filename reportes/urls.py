
from django.urls import path

from reportes.views import Reporte_actividad

urlpatterns = [
    path('actividad/', Reporte_actividad.as_view(), name="Reporte_act"),

]