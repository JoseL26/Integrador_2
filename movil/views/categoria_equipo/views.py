from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator

from movil.forms import CategiaEquipoForm
from movil.models import CaterogiaEquipo


def CategoriaListEq(request):
    data = {
        'titulo': 'Listado de categoria de equipos',
        'categoria_equipos': CaterogiaEquipo.objects.all()
    }
    return render(request, 'categoria_equipo/listar_cat_equipo.html', data)


class Categori_Lista_Equipo(ListView):
    model = CaterogiaEquipo
    template_name = 'categoria_equipo/listar_cat_equipo.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = CaterogiaEquipo.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = 'Listado de categoria de equipos'
        context['create_url'] = reverse_lazy('movil:CategoraCreatet_Eq')
        context['list_url'] = reverse_lazy('movil:CategoriaListEq')
        context['entity'] = 'CaterogiaEquipos'
        return context


class CategoriaCreateEq(CreateView):
    model = CaterogiaEquipo
    form_class = CategiaEquipoForm
    template_name = 'categoria/crear_categoria.html'
    success_url = reverse_lazy('movil:CategoriaListEq')

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
        context['titulo'] = 'Registro de categorias de equipos'
        context['entity'] = 'CaterogiaEquipos'
        context['list_url'] = reverse_lazy('movil:CategoriaListEq')
        context['action'] = 'add'
        return context

class CategoriaUpdateEq(UpdateView):
    model = CaterogiaEquipo
    form_class = CategiaEquipoForm
    template_name = 'categoria/crear_categoria.html'
    success_url = reverse_lazy('movil:CategoriaListEq')

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
        context['titulo'] = 'Edición de categoria de equipos'
        context['entity'] = 'CaterogiaEquipos'
        context['list_url'] = reverse_lazy('movil:CategoriaListEq')
        context['action'] = 'edit'
        return context