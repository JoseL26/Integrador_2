from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from datetime import datetime

from movil.models import ParteHoras, Empleado


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        request.user.get_group_session()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'get_reporte_horas_año_mes':
                data = self.get_reporte_horas_año_mes()
            #elif action == 'get_reporte_horas_trabajador_mes':
            #    data = self.get_reporte_horas_trabajador_mes()

            else:
                data['error'] = 'a ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_reporte_horas_año_mes(self):
        data = []
        try:
            año = datetime.now().year
            for m in range(1, 13):
                total = ParteHoras.objects.filter(fecha__year=año, fecha__month=m).aggregate(r=Coalesce(Sum('TotalHoras'),0)).get('r')
                data.append(float(total))
        except:
            pass
        return data


    def get_context_data(self, **kwargs):
        contex=super().get_context_data(**kwargs)
        contex['panel'] = 'Panel de administrador'
        contex['reporte_horas_año_mes'] = self.get_reporte_horas_año_mes()
        return contex