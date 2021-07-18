from django.contrib.auth.decorators import login_required
import json
import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.utils.decorators import method_decorator
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

from movil.forms import ParteHorasForm
from movil.mixin import ValidatePermissionRequiredMixin
from movil.models import ParteHoras, Equipo, OrdenTrabajo, DetParte


class Parte_horas_list(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = ParteHoras
    template_name = 'actividades/listar_actividades.html'
    permission_required = 'view_partehoras'

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
            elif action == 'search_details_parte':
                data = []
                for i in DetParte.objects.filter(parte_id=request.POST['id']):
                    data.append(i.toJSON())
            else:
                data['error'] = 'ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = 'Listado de Parte de horas'
        context['create_url'] = reverse_lazy('movil:ParteCreate')
        context['list_url'] = reverse_lazy('movil:PhorasList')
        context['entity'] = 'ParteHoras'
        return context


class Parte_horas_create(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = ParteHoras
    form_class = ParteHorasForm
    template_name = 'actividades/crear_actividades.html'
    success_url = reverse_lazy('movil:PhorasList')
    permission_required = "add_partehoras"
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'buscar_productos':
                data = []
                orden = OrdenTrabajo.objects.filter(Orden__icontains=request.POST['term'])[0:10]
                for i in orden:
                    item = i.toJSON()
                    item['value'] = i.Orden
                    data.append(item)
                    # insertando datos a parte de horas
            elif action == 'add':
                with transaction.atomic():
                    tareas = json.loads(request.POST['tareas'])
                    partehora = ParteHoras()
                    partehora.Empleado_id = tareas['Empleado']
                    partehora.fecha = tareas['fecha']
                    partehora.TotalHoras = float(tareas['TotalHoras'])
                    partehora.save()
                    for i in tareas['actividades']:
                        detalle = DetParte()
                        detalle.parte_id = partehora.id
                        detalle.Orden_id = i['Orden']
                        detalle.operacion = int(i['operacion'])
                        detalle.desc_actividad = str(i['desc_actividad'])
                        detalle.Cantidad = float(i['Cantidad'])
                        detalle.save()
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
        context['det'] = []
        return context


class Parte_horas_update(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = ParteHoras
    form_class = ParteHorasForm
    template_name = 'actividades/crear_actividades.html'
    success_url = reverse_lazy('movil:PhorasList')
    permission_required = "change_partehoras"
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'buscar_productos':
                data = []
                orden = OrdenTrabajo.objects.filter(Orden__icontains=request.POST['term'])[0:10]
                for i in orden:
                    item = i.toJSON()
                    item['value'] = i.Orden
                    data.append(item)
                    # Editando datos a parte de horas
            elif action == 'edit':
                with transaction.atomic():
                    tareas = json.loads(request.POST['tareas'])
                    partehora = self.get_object()
                    partehora.Empleado_id = tareas['Empleado']
                    partehora.fecha = tareas['fecha']
                    partehora.TotalHoras = float(tareas['TotalHoras'])
                    partehora.save()
                    partehora.detparte_set.all().delete()
                    for i in tareas['actividades']:
                        detalle = DetParte()
                        detalle.parte_id = partehora.id
                        detalle.Orden_id = i['Orden']
                        detalle.operacion = int(i['operacion'])
                        detalle.desc_actividad = str(i['desc_actividad'])
                        detalle.Cantidad = float(i['Cantidad'])
                        detalle.save()
            else:
                data['error'] = 'no ha ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def ge_parte_datlle(self):
        data = []
        try:
            for i in DetParte.objects.filter(parte_id=self.get_object().id):
                item = i.Orden.toJSON()
                item['operacion'] = int(i.operacion)
                item['desc_actividad'] = str(i.desc_actividad)
                item['Cantidad'] = float(i.Cantidad)
                data.append(item)
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = 'Edición de Horas'
        context['entity'] = 'ParteHoras'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        context['det'] = json.dumps(self.ge_parte_datlle())
        return context


class Parte_horas_delete(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = ParteHoras
    template_name = 'actividades/eliminar.html'
    success_url = reverse_lazy('movil:PhorasList')
    permission_required = 'delete_partehoras'
    url_redirect = success_url

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
        context['title'] = 'Eliminación de un parte de hora'
        context['entity'] = 'ParteHoras'
        context['list_url'] = self.success_url
        return context


class generarPDF_parte(View):
    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """

        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        try:
            template = get_template('actividades/crear_pdf.html')
            context = {
                'Phora': ParteHoras.objects.get(pk=self.kwargs['pk']),
                'emp': {'name': 'SAN MARTIN CONTRATISTAS S.A.', 'ruc': '10101010121', 'direccion': 'Jr. Morro Solar, Lima'},
                'icon': '{}{}'.format(settings.MEDIA_URL, 'logo.png')
            }
            html = template.render(context)
            # Create a Django response object, and specify content_type as pdf
            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

            # create a pdf
            pisa_status = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback
            )
            return response
        except:
            pass
        # if error then show some funy view
        return HttpResponseRedirect(reverse_lazy('movil:PhorasList'))
