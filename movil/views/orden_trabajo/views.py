from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView,UpdateView

from movil.forms import OrdenTrabajoForm
from movil.models import OrdenTrabajo

def OrdenList(request):
    data = {
        'titulo': 'Listado de Ordenes',
        'ordenes': OrdenTrabajo.objects.all()
    }
    return render(request, 'orden_de_trabajo/listar_orden.html', data)

class Orden_Lista(ListView):
    model = OrdenTrabajo
    template_name = 'orden_de_trabajo/listar_orden.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = OrdenTrabajo.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = 'Listado de ordenes'
        context['create_url'] = reverse_lazy('movil:OrdenCreate')
        context['list_url'] = reverse_lazy('movil:OrdenList')
        context['entity'] = 'Ordenes'
        return context

class OrdenCreate(CreateView):
    model = OrdenTrabajo
    form_class = OrdenTrabajoForm
    template_name = 'orden_de_trabajo/crear_orden.html'
    success_url = reverse_lazy('movil:OrdenList')

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
        context['titulo'] = 'Registro de Ordenes'
        context['entity'] = 'Ordenes'
        context['list_url'] = reverse_lazy('movil:OrdenList')
        context['action'] = 'add'
        return context

class OrdenUpdate(UpdateView):
    model = OrdenTrabajo
    form_class = OrdenTrabajoForm
    template_name = 'orden_de_trabajo/crear_orden.html'
    success_url = reverse_lazy('movil:OrdenList')

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
        context['titulo'] = 'Edición de ordenes de trabajo'
        context['entity'] = 'Ordenes'
        context['list_url'] = reverse_lazy('movil:OrdenList')
        context['action'] = 'edit'
        return context