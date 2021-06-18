from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from movil.forms import ParteHorasForm
from movil.models import ParteHoras, Equipo


class Parte_horas_lis(ListView):
    model = ParteHoras
    template_name = 'actividades/crear_actividades.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in ParteHoras.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'a ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = 'Listado de Parte de horas'
        context['create_url'] = reverse_lazy('movil:ParteHorasCreate')
        context['list_url'] = reverse_lazy('movil:ParteHorasList')
        context['entity'] = 'ParteHoras'
        return context


class Parte_horas_create(CreateView):
    model = ParteHoras
    form_class = ParteHorasForm
    template_name = 'actividades/crear_actividades.html'
    success_url = reverse_lazy('index')
    permission_required = "movil.add_actividades"
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'buscar_productos':
                data =[]
                equipo = Equipo.objects.filter(Cod_equipo__icontains=request.POST['term'])
                for i in equipo:
                    item = i.toJSON()
                    item['value'] = i.Cod_equipo
                    data.append(item)
            else:
                data['error'] = 'no ha ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = 'Registro de Horas'
        context['entity'] = 'ParteHoras'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

