from django.views.generic import TemplateView

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        contex=super().get_context_data(**kwargs)
        contex['panel'] = 'Panel de administrador'
        return contex