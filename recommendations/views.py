from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PerfilUsuarioForm, RegistroSencilloForm

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroSencilloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroSencilloForm()
    
    return render(request, 'recommendations/registro_usuario.html', {'form': form})

@login_required
def registroPerfil(request):
    if request.method == 'POST':
        form = PerfilUsuarioForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            print(f"Datos recibidos de {request.user.username}: {datos}")
            return render(request, 'recommendations/exito.html', {'nombre': datos['nombre']})
    else:
        form = PerfilUsuarioForm()
    
    return render(request, 'recommendations/perfil_form.html', {'form': form})
# Create your views here.
