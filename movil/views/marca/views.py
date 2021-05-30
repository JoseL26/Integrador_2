from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator

from movil.forms import MarcaEquipoForm
from movil.models import Marca


def MarcaListEq(request):
    data = {
        'titulo': 'Listado de marca de equipos',
        'marcas': Marca.objects.all()
    }
    return render(request, 'marca/lista_marca.html', data)


class Marca_Lista_Equipo(ListView):
    model = Marca
    template_name = 'marca/lista_marca.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Marca.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = 'Listado de marca de equipos'
        context['create_url'] = reverse_lazy('movil:MarcaCreate_Eq')
        context['list_url'] = reverse_lazy('movil:MarcaListEq')
        context['entity'] = 'Marcas'
        return context


class MarcaCreateEq(CreateView):
    model = Marca
    form_class = MarcaEquipoForm
    template_name = 'marca/crear_marca.html'
    success_url = reverse_lazy('movil:MarcaListEq')

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
        context['titulo'] = 'Registro de marca de equipos'
        context['entity'] = 'Marcas'
        context['list_url'] = reverse_lazy('movil:MarcaListEq')
        context['action'] = 'add'
        return context

class MarcaUpdateEq(UpdateView):
    model = Marca
    form_class = MarcaEquipoForm
    template_name = 'marca/crear_marca.html'
    success_url = reverse_lazy('movil:MarcaListEq')

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
        context['titulo'] = 'Edición de marca de equipos'
        context['entity'] = 'Marcas'
        context['list_url'] = reverse_lazy('movil:MarcaListEq')
        context['action'] = 'edit'
        return context