from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator

from movil.forms import CategoriaForm
from movil.models import Categoria


def CategoriaList(request):
    data = {
        'titulo': 'Listado de categorias',
        'categorias': Categoria.objects.all()
    }
    return render(request, 'categoria/categoria_lista.html', data)


class Categori_Lista(ListView):
    model = Categoria
    template_name = 'categoria/categoria_lista.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Categoria.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = 'Listado de categorias'
        context['create_url'] = reverse_lazy('movil:Categoriacreate')
        context['list_url'] = reverse_lazy('movil:CategoriaList')
        context['entity'] = 'Categorias'
        return context


class CategoriaCreate(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/crear_categoria.html'
    success_url = reverse_lazy('movil:CategoriaList')

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

    #    print(request.POST)
    #    form=CategoriaForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    #        return HttpResponseRedirect(self.success_url)
    #    self.object = None
    #    contex = self.get_context_data(**kwargs)
    #    contex['form'] = form
    #    return render(request, self.template_name, contex)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = 'Registro de categorias'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('movil:CategoriaList')
        context['action'] = 'add'
        return context

class CategoriaUpdate(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/crear_categoria.html'
    success_url = reverse_lazy('movil:CategoriaList')

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