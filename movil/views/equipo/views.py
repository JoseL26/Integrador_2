from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from movil.mixin import ValidatePermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator

from movil.forms import EquipoForm
from movil.models import Equipo

class Lista_Equipo(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    permission_required = 'view_equipo'
    model = Equipo
    template_name = 'equipo/lista_equipo.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Equipo.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = 'Listado de equipos'
        context['create_url'] = reverse_lazy('movil:Create_Equipo')
        context['list_url'] = reverse_lazy('movil:Lista_Equipo')
        context['entity'] = 'Equipos'
        return context


class Create_Equipo(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    permission_required = 'add_equipo'
    model = Equipo
    form_class = EquipoForm
    template_name = 'equipo/crear_equipo.html'
    success_url = reverse_lazy('movil:Lista_Equipo')

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
        context['titulo'] = 'Registro de equipo'
        context['entity'] = 'Equipos'
        context['list_url'] = reverse_lazy('movil:Lista_Equipo')
        context['action'] = 'add'
        return context

class Update_Equipo(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    permission_required = 'change_equipo'
    model = Equipo
    form_class = EquipoForm
    template_name = 'equipo/crear_equipo.html'
    success_url = reverse_lazy('movil:Lista_Equipo')

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
        context['titulo'] = 'Edición de equipo'
        context['entity'] = 'Equipos'
        context['list_url'] = reverse_lazy('movil:Lista_Equipo')
        context['action'] = 'edit'
        return context