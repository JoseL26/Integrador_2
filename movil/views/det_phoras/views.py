from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView,UpdateView

from movil.forms import DetPHorasForm
from movil.models import DetalleParte

class DetPhoras_Lista(ListView):
    model = DetalleParte
    template_name = 'det_phoras/lista_detphoras.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = OrdenTrabajo.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = 'Listado de Detalle de Parte de Horas'
        context['create_url'] = reverse_lazy('movil:DetPhorasCreate')
        context['list_url'] = reverse_lazy('movil:DetPhorasList')
        context['entity'] = 'DetallePartes'
        return context
        
#---Falla al momento de crear un detalle---
class DetPhoras_Create(CreateView):
    model = DetalleParte
    form_class = DetPHorasForm
    template_name = 'det_phoras/crear_detphoras.html'
    success_url = reverse_lazy('movil:DetPhorasList')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'no ha ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = 'Registro de Detalle de Parte de Horas'
        context['entity'] = 'DetallePartes'
        context['list_url'] = reverse_lazy('movil:DetPhorasList')
        context['action'] = 'add'
        return context

class DetPhoras_Update(UpdateView):
    model = DetalleParte
    form_class = DetPHorasForm
    template_name = 'det_phoras/crear_detphoras.html'
    success_url = reverse_lazy('movil:DetPhorasList')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'no ha ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = 'Edición de Detalle de Parte de Horas'
        context['entity'] = 'DetallePartes'
        context['list_url'] = reverse_lazy('movil:DetPhorasList')
        context['action'] = 'edit'
        return context