from django import forms
from django.forms import ModelForm, TextInput

from .models import *

#Formulario de empleado
class FormularioEmpleado(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #    form.field.widget.attrs['class'] = 'form-control'
        #    form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['Apellidos'].widget.attrs['autofocus'] = True

    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'Apellidos': TextInput(
                attrs={
                    'placeholder': 'Ingrese de categoria'
                }
            ),
            'Nombres': TextInput(
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

#formulario de categoria
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

#formulario de cargo
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

#formulario de categoria de equipo
class CategiaEquipoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #    form.field.widget.attrs['class'] = 'form-control'
        #    form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['Desc_categoria'].widget.attrs['autofocus'] = True

    class Meta:
        model = CaterogiaEquipo
        fields = '__all__'
        labels = {
            'Desc_categoria': 'Categoria equipo',

        }
        widgets = {
            'Desc_categoria': TextInput(
                attrs={
                    'placeholder': 'Ingrese categoria de equipo'
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

#formulario de marca de equipo
class MarcaEquipoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #    form.field.widget.attrs['class'] = 'form-control'
        #    form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['Desc_marca'].widget.attrs['autofocus'] = True

    class Meta:
        model = Marca
        fields = '__all__'
        labels = {
            'Desc_marca': 'Marca equipo',

        }
        widgets = {
            'Desc_marca': TextInput(
                attrs={
                    'placeholder': 'Ingrese marca de equipo'
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

#formulario de marca de equipo
class EquipoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #    form.field.widget.attrs['class'] = 'form-control'
        #    form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['Cod_equipo'].widget.attrs['autofocus'] = True

    class Meta:
        model = Equipo
        fields = '__all__'
        labels = {
            'Cod_equipo': 'Codigo equipo',
            'Desc_equipo': 'Descripción equipo',
            'CaterogiaEq': 'Categoria',

        }
        widgets = {
            'Cod_equipo': TextInput(
                attrs={
                    'placeholder': 'Ingrese codigo de equipo'
                }
            ),
            'Desc_equipo': TextInput(
                attrs={
                    'placeholder': 'Ingrese descripción de equipo'
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

class OrdenTrabajoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #    form.field.widget.attrs['class'] = 'form-control'
        #    form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['Orden'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = OrdenTrabajo
        fields = '__all__'
        labels = {
            'eq_sistema': 'Sistema',
            'desc_conjunto': 'Descripcion'
        }
        widgets = {
            'Orden': TextInput(
                attrs={
                    'placeholder': 'Ingrese la Orden'
                }
            ),
            
            'eq_sistema': TextInput(
                attrs={
                    'placeholder': 'Ingrese un sistema'
                }
            ),
            'conjunto': TextInput(
                attrs={
                    'placeholder': 'Ingrese un conjunto'
                }
            ),
            'desc_conjunto': TextInput(
                attrs={
                    'placeholder': 'Ingrese desc'
                }
            ),
            'fase': TextInput(
                attrs={
                    'placeholder': 'Ingrese una fase'
                }
            ),
            
            'estado': TextInput(
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

class UsuarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #    form.field.widget.attrs['class'] = 'form-control'
        #    form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['usuario'].widget.attrs['autofocus'] = True

    class Meta:
        model = Usuario
        fields = '__all__'
        labels = {
            'usuario': 'Usuario',
            'clave': 'Contraseña'
        }
        widgets = {
            'usuario': TextInput(
                attrs={
                    'placeholder': 'Ingrese de cargo'
                }
            ),
            'clave': TextInput(
                attrs={
                    'placeholder': 'Ingrese de área'
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