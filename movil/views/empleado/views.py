from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from movil.models import Categoria,Empleado
from movil.forms import FormularioEmpleado, CategoriaForm
from django.core.mail import send_mail
#
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
#
import datetime

# Create your views here.
def home(request):
    return render(request,'base.html')

def categoria(request):
    return render(request,'categorias.html')

#categoria listado --
def CategoriaList(request):
    data = {
        'titulo': 'Listado de categorias',
        'categorias': Categoria.objects.all()
    }
    return render(request, 'categoria_lista.html', data)


class Categori_Lista(ListView):
    model = Categoria
    template_name = 'categoria_lista.html'

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
    template_name = 'crear_categoria.html'
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
#cierra categoria listado

def crear_categoria(request):
    return render(request,'crear_categoria.html')

def cargo(request):
    return render(request,'cargos_trabajador.html')

def prueba(request):
    return render(request,'inicio.html')

def crear_usuario(request):
    return render(request, 'crear_usuario.html')

def buscar(request):
    errors=[]
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if len(q)<1:
            errors.append('Por favor ingrese un criterio de busqueda')
        elif len(q)>20:
            errors.append('Ingrese menos de 20 digitos')
        else:
            categoria = Categoria.objects.filter(Descripcion__icontains=q)
            return render(request, 'resultados.html', {'categoria':categoria,'query':q})
    return render(request, 'formulario_buscar.html',{'errors':errors})

def Fecha_actual(request):
    ahora= datetime.datetime.now()
    return render(request, 'fecha_actual.html', {'fecha_actual':ahora})

def horas_adelante(request, horas):
    try:
        horas = int(horas)
    except ValueError:
        raise Http404()
    dt= datetime.datetime.now()+datetime.timedelta(hours=horas)
    return render(request,'horas_adelante.html',{'hora_siguiente':dt, 'horas':horas})

def empleado(request):
    if request.method=='POST':
        form=FormularioEmpleado(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            Ape=cd.get('Apellidos')
            Nom=cd.get('Nombres')
            dni=cd.get('DNI')
            dir=cd.get('Direccion')
            dist=cd.get('Distrito')
            prov=cd.get('Provincia')
            telf=cd.get('Telefono')
            corre=cd.get('Correo')
            cat=cd.get('Categoria')
            carg=cd.get('Cargo')
            est=cd.get('Estado')

            obj=Empleado.objects.create(Apellidos=Ape, Nombres=Nom,DNI=dni,Direccion=dir,Distrito=dist,
                                        Provincia=prov,Telefono=telf,Correo=corre, categorias=cat,
                                        cargos=carg,Estado=est)

            return HttpResponseRedirect('/list_emp/')
    else:
        form= FormularioEmpleado()

    return render(request, 'empleado.html',{'form':form})

def ListaEmpleado(request):
    lista=Empleado.objects.all()
    return render(request, 'lista_empleado.html', {'lista':lista})
