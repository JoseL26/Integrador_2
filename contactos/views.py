from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from contactos.forms import FormularioContactos

# Create your views here.
def Index(request):
    hola="Bienvenidos a mi pagina"
    return render(request, 'inicio.html')

def contactos(request):

    if request.method=='POST':
        form=FormularioContactos(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            send_mail(request.POST['asunto'], request.POST['mensaje'],
                      request.POST.get('email','nmpc.629@gmail.com'),
                      ['amor_mio65@hotmail.com'])
            return HttpResponseRedirect('/contactos/')
    else:
        form=FormularioContactos()
    return render(request, 'forulario-contactos.html', {'form':form})