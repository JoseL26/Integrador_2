from django import forms
class FormularioContactos(forms.Form):
    asunto=forms.CharField(max_length=70)
    email=forms.EmailField(required=False, label='Tu correo electronico')
    mensaje=forms.CharField(widget=forms.Textarea)

    def clean_mensaje(self):
        mensaje=self.cleaned_data['mensaje']
        num_palabras=len(mensaje.split())
        if num_palabras<4:
            raise forms.ValidationError("¡Se requiere minimo 4 palabras!")
        return mensaje