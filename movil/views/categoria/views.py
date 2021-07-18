from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.utils.decorators import method_decorator

from movil.forms import CategoriaForm
from movil.mixin import isSuperusermixin, ValidatePermissionRequiredMixin
from movil.models import Categoria

class Categori_Lista(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    permission_required = 'view_categoria'
    model = Categoria
    template_name = 'categoria/categoria_lista.html'

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Categoria.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'a ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = 'Listado de categorias'
        context['create_url'] = reverse_lazy('movil:Categoriacreate')
        context['list_url'] = reverse_lazy('movil:CategoriaList')
        context['entity'] = 'Categorias'
        return context


class CategoriaCreate(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    permission_required = 'add_categoria'
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/crear_categoria.html'
    success_url = reverse_lazy('movil:CategoriaList')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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
        context['titulo'] = 'Registro de categorias'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('movil:CategoriaList')
        context['action'] = 'add'
        return context

class CategoriaUpdate(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    permission_required = 'change_categoria'
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/crear_categoria.html'
    success_url = reverse_lazy('movil:CategoriaList')

    @method_decorator(login_required)
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
        context['titulo'] = 'Edición de categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('movil:CategoriaList')
        context['action'] = 'edit'
        return context

class CategoriaDelete(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    permission_required = 'delete_categoria'
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/eliminar.html'
    success_url = reverse_lazy('movil:CategoriaList')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = 'Eliminación de categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('movil:CategoriaList')
        return context

class CategoriaFormView(FormView):
    form_class = CategoriaForm
    template_name = 'categoria/crear_categoria.html'
    success_url = reverse_lazy('movil:CategoriaList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = 'Lista de categorias'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('movil:CategoriaList')
        context['action'] = 'add'
        return context