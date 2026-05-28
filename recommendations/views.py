import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PerfilUsuarioForm, RegistroSencilloForm

from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, XSD

HO = Namespace("http://www.newhobbies.org/ontology/")

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
            
            g = Graph()
            ruta_archivo_rdf = "perfiles_usuarios.ttl"
            ruta_hobbies = "hobbies_base.ttl"
            
            if os.path.exists(ruta_archivo_rdf):
                g.parse(ruta_archivo_rdf, format="turtle")
            
            g.bind("ho", HO)
            usuario_uri = URIRef(HO + request.user.username)
            
            g.add((usuario_uri, RDF.type, HO.Persona))
            g.add((usuario_uri, HO.nombre, Literal(datos['nombre'], datatype=XSD.string)))
            
            nivel_uri = URIRef(HO + datos['nivel_experiencia'])
            g.add((usuario_uri, HO.tieneNivel, nivel_uri))
            
            for interes in datos['intereses']:
                g.add((usuario_uri, HO.tieneInteres, URIRef(HO + interes)))
                
            for habilidad in datos['habilidades']:
                g.add((usuario_uri, HO.poseeHabilidad, URIRef(HO + habilidad)))
                
            for rasgo in datos['rasgos']:
                g.add((usuario_uri, HO.tieneRasgo, URIRef(HO + rasgo)))
            
            g.serialize(destination=ruta_archivo_rdf, format="turtle")
            
            if os.path.exists(ruta_hobbies):
                g.parse(ruta_hobbies, format="turtle")
                
            consulta_sparql = f"""
                PREFIX ho: <http://www.newhobbies.org/ontology/>
                SELECT DISTINCT ?nombreHobbie
                WHERE {{
                    ho:{request.user.username} ho:tieneInteres ?interes .
                    ho:{request.user.username} ho:poseeHabilidad ?habilidad .
                    
                    ?hobbie a ho:Hobbie ;
                            ho:nombreHobbie ?nombreHobbie ;
                            ho:requiereInteres ?interes ;
                            ho:requiereHabilidad ?habilidad .
                }}
            """
            
            
            resultados = g.query(consulta_sparql)
            lista_recomendaciones = [fila.nombreHobbie.value for fila in resultados]
            
           
            if len(lista_recomendaciones) == 0:
                lista_recomendaciones = ["Aún no encontramos un match perfecto, ¡intenta agregar más intereses!"]
            
            
            
            return render(request, 'recommendations/exito.html', {
                'nombre': datos['nombre'],
                'recomendaciones': lista_recomendaciones
            })
    else:
        form = PerfilUsuarioForm()
    
    return render(request, 'recommendations/perfil_form.html', {'form': form})

def inicio(request):
    return render(request, 'recommendations/inicio.html')
# Create your views here.
