from django.forms import *


class ReportForm(Form):

    range_date = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off'
    }))