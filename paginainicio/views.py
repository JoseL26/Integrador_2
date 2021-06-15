from django.views.generic import TemplateView

from django.shortcuts import render

# Create your views here.
class Create_index_view(TemplateView):
    template_name = 'index.html'