from django.shortcuts import render
from .forms import PerfilUsuarioForm


def registroPerfil(request):
    if request.method == 'POST':
        form = PerfilUsuarioForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            print(f"Datos recibidos: {datos}")
            
            return render(request, 'recommendations/exito.html', {'nombre': datos['nombre']})
    else:
        form = PerfilUsuarioForm()
    
    return render(request, 'recommendations/perfil_form.html', {'form': form})
# Create your views here.
