from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView,UpdateView

from movil.forms import ParteHorasForm 
from movil.models import ParteHoras

class Phoras_Lista(ListView):
    model = ParteHoras
    template_name = 'parte_horas/lista_phoras.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = ParteHoras.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = 'Listado de Parte de Horas'
        context['create_url'] = reverse_lazy('movil:PhorasCreate')
        context['list_url'] = reverse_lazy('movil:PhorasList')
        context['entity'] = 'ParteHoras'
        return context

class Phoras_Create(CreateView):
    model = ParteHoras
    form_class = ParteHorasForm
    template_name = 'parte_horas/crear_phoras.html'
    success_url = reverse_lazy('movil:PhorasList')

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
        context['titulo'] = 'Registro de Parte de Horas'
        context['entity'] = 'ParteHoras'
        context['list_url'] = reverse_lazy('movil:PhorasList')
        context['action'] = 'add'
        return context

class Phoras_Update(UpdateView):
    model = ParteHoras
    form_class = ParteHorasForm
    template_name = 'parte_horas/crear_phoras.html'
    success_url = reverse_lazy('movil:PhorasList')

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
        context['titulo'] = 'Edición de Parte de Horas'
        context['entity'] = 'ParteHoras'
        context['list_url'] = reverse_lazy('movil:PhorasList')
        context['action'] = 'edit'
        return context