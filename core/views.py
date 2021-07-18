from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class CadastroView(TemplateView):
    template_name = 'cadastro.html'


class HomeView(TemplateView):
    template_name = 'index.html'

