from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from movil.forms import ListaForm
from movil.models import *


class TestView(TemplateView):
    template_name = 'listaspro.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_CaterogiaEquipo_id':
                data = [{'id': '', 'text': '------------'}]
                for i in Equipo.objects.filter(cat_id=request.POST['id']):
                    data.append({'id': i.Cod_equipo, 'text': i.Desc_equipo, 'data': i.CaterogiaEq.toJSON()})
            elif action == 'autocomplete':
                data = []
                for i in Categoria.objects.filter(name__icontains=request.POST['term'])[0:10]:
                    item = i.toJSON()
                    item['text'] = i.name
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Select Aninados | Django'
        context['form'] = ListaForm()
        return context
