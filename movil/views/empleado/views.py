from movil.forms import FormularioEmpleado
from movil.models import Categoria, Empleado
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator

class Empleado_Lista(ListView):
    model = Empleado
    template_name = 'empleado/lista_empleado.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Empleado.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = 'Listado de empleados'
        context['create_url'] = reverse_lazy('movil:Crear_Empleado')
        context['list_url'] = reverse_lazy('movil:ListaEmpleado')
        context['entity'] = 'Empleados'
        return context

class Empleado_Create(CreateView):
    model = Empleado
    form_class = FormularioEmpleado
    template_name = 'empleado/empleado.html'
    success_url = reverse_lazy('movil:ListaEmpleado')

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
        context['titulo'] = 'Registro de empleados'
        context['entity'] = 'Empleados'
        context['list_url'] = reverse_lazy('movil:ListaEmpleado')
        context['action'] = 'add'
        return context

class Empleado_Update(UpdateView):
    model = Empleado
    form_class = FormularioEmpleado
    template_name = 'empleado/empleado.html'
    success_url = reverse_lazy('movil:ListaEmpleado')

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
        context['titulo'] = 'Edición de empleado'
        context['entity'] = 'Empleados'
        context['list_url'] = reverse_lazy('movil:ListaEmpleado')
        context['action'] = 'edit'
        return context

