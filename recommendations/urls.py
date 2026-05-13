from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='recommendations/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('crear-cuenta/', views.registro_usuario, name='registro_usuario'),
    path('perfil/', views.registroPerfil, name='registro_perfil'),
]