from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView,UpdateView

from movil.forms import UsuarioForm
from movil.models import Usuario

class Usuario_Lista(ListView):
    model = Usuario
    template_name = 'usuario/listar_usuario.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Usuario.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = 'Listado de usuarios'
        context['create_url'] = reverse_lazy('movil:UsuarioCreate')
        context['list_url'] = reverse_lazy('movil:UsuarioList')
        context['entity'] = 'Usuarios'
        return context

class UsuarioCreate(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/crear_usuario.html'
    success_url = reverse_lazy('movil:UsuarioList')

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
        context['titulo'] = 'Registro de Ordenes'
        context['entity'] = 'Usuarios'
        context['list_url'] = reverse_lazy('movil:UsuarioList')
        context['action'] = 'add'
        return context

class UsuarioUpdate(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/crear_usuario.html'
    success_url = reverse_lazy('movil:UsuarioList')

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
        context['titulo'] = 'Edición de usuarios'
        context['entity'] = 'Usuarios'
        context['list_url'] = reverse_lazy('movil:UsuarioList')
        context['action'] = 'edit'
        return context