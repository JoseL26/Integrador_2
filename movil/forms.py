from django import forms
from django.forms import ModelForm, TextInput

from .models import Categoria, Cargo
class FormularioEmpleado(forms.Form):
    Apellidos = forms.CharField(min_length="6")
    Nombres= forms.CharField(min_length="3")
    DNI= forms.IntegerField()
    Direccion=forms.CharField()
    Distrito=forms.CharField()
    Provincia=forms.CharField(max_length="20", min_length="3")
    Telefono=forms.IntegerField(required=True)
    Correo=forms.EmailField(required=True)
    Categoria=forms.ModelChoiceField(queryset=Categoria.objects.all())
    Cargo=forms.ModelChoiceField(queryset=Cargo.objects.all())
    Estado=forms.CharField()

class CategoriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #for form in self.visible_fields():
        #    form.field.widget.attrs['class'] = 'form-control'
        #    form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['Descripcion'].widget.attrs['autofocus'] = True

    class Meta:
        model = Categoria
        fields = '__all__'
        labels ={
            'Estado': 'Estado'
        }

        widgets = {
            'Descripcion': TextInput(
                attrs={
                    'placeholder': 'Ingrese de categoria'
                }
            ),
            'Estado': TextInput(
                attrs={
                    'placeholder': 'Ingrese de Estado 1 o 0',
                    'maxlength': '1',
                    'aria-valuemax': '1'
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class CargoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #    form.field.widget.attrs['class'] = 'form-control'
        #    form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['Descripcion'].widget.attrs['autofocus'] = True

    class Meta:
        model = Cargo
        fields = '__all__'
        labels = {
            'Descripcion': 'Cargo',
            'Departament': 'Área'
        }
        widgets = {
            'Descripcion': TextInput(
                attrs={
                    'placeholder': 'Ingrese de cargo'
                }
            ),
            'Departament': TextInput(
                attrs={
                    'placeholder': 'Ingrese de área'
                }
            ),

            'Estado': TextInput(
                attrs={
                    'placeholder': 'Ingrese de Estado 1 o 0',
                    'maxlength': '1',
                    'aria-valuemax': '1'
                }
            )
        }
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data