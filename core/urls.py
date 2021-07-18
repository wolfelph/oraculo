from django.urls import path, include
from django.contrib.auth import views as auth_views

from core.views import IndexView, LoginView, CadastroView, HomeView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Utilizando a propria do django
    path('social-auth/', include('social_django.urls', namespace='social')),  # Autenticando pelo social
    path('', IndexView.as_view(), name='index'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('home/', HomeView.as_view(), name='index'),
]