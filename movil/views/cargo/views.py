from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView,UpdateView

from movil.forms import CargoForm
from movil.models import Cargo


def CargoList(request):
    data = {
        'titulo': 'Listado de cargos',
        'categorias': Cargo.objects.all()
    }
    return render(request, 'cargo/cargo_lista.html', data)

class Cargo_Lista(ListView):
    model = Cargo
    template_name = 'cargo/cargo_lista.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Cargo.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = 'Listado de cargos'
        context['create_url'] = reverse_lazy('movil:Cargocreate')
        context['list_url'] = reverse_lazy('movil:Cargolist')
        context['entity'] = 'Cargos'
        return context


class CargoCreate(CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'cargo/cargo_crear.html'
    success_url = reverse_lazy('movil:Cargolist')

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
        context['titulo'] = 'Registro de cargos'
        context['entity'] = 'Cargos'
        context['list_url'] = reverse_lazy('movil:Cargolist')
        context['action'] = 'add'
        return context

class CargoUpdate(UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'cargo/cargo_crear.html'
    success_url = reverse_lazy('movil:Cargolist')

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
        context['list_url'] = reverse_lazy('movil:Cargolist')
        context['action'] = 'edit'
        return context