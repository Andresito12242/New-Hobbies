from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registroPerfil, name='registro_perfil'),
]