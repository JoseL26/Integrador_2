from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from movil.models import ParteHoras
from reportes.forms import ReportForm

from django.db.models.functions import Coalesce
from django.db.models import Sum

class Reporte_actividad(TemplateView):
    template_name = 'actividades/reporte.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_reporte':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                buscar = ParteHoras.objects.all()
                if len(start_date) and len(end_date):
                    buscar = buscar.filter(fecha__range=[start_date, end_date])
                for i in buscar:
                    data.append([
                        i.id,
                        i.Empleado.Apellidos,
                        i.Empleado.Nombres,
                        i.fecha.strftime('%Y-%m-%d'),
                        format(i.TotalHoras, '.2f'),
                    ])
                total = buscar.aggregate(r=Coalesce(Sum('TotalHoras'), 0)).get('r')
                data.append([
                    '---',
                    '---',
                    '---',
                    '---',
                    format(total, '.2f'),

                ])
            else:
                data['error'] = 'a ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Reporte de actividades'
        context['list_url'] = reverse_lazy('Reporte_act')
        context['entity'] = 'Reportes'
        context['form'] = ReportForm()
        return context
