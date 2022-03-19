from django.http import HttpResponse
from django.shortcuts import render

from .models import Lector,Bloggero,Empresa
from .forms import lector_formulario,bloggero_formulario,empresa_formulario,lector_busqueda,bloggero_busqueda,empresa_busqueda

def usuario(request):
    return render(request, "usuario.html",{})




def registro(request):
    return render(request, "registro/registro.html", {})

def crear_lectores(request):
    if request.method=="POST":
        form=lector_formulario(request.POST)

        if form.is_valid():
            data= form.cleaned_data
            lector= Lector(nombre_anonimo=data['nombre_anonimo'],pais_de_residencia=data['pais_de_residencia'],correo_electronico=data['correo_electronico'])
            lector.save()
            return render(request, 'inicio.html', {})

    form=lector_formulario
    return render(request, "registro/registro-bloggeros.html",{'form':form})


def crear_bloggeros(request):
    if request.method=="POST":
        form=bloggero_formulario(request.POST)

        if form.is_valid():
            data= form.cleaned_data
            bloggero= Bloggero(nombre=data['nombre'],apellido=data['apellido'],alias=data['alias'],pais_de_residencia=data['pais_de_residencia'],correo_electronico=data['correo_electronico'])
            bloggero.save()
            return render(request, 'inicio.html', {})

    form=bloggero_formulario
    return render(request, "registro/registro-bloggeros.html",{'form':form})


def crear_empresas(request):
    if request.method=="POST":
        form=empresa_formulario(request.POST)

        if form.is_valid():
            data= form.cleaned_data
            empresa= Empresa(nombre_de_empresa=data['nombre_de_empresa'],rubro=data['rubro'],cuit=data['cuit'],correo_electronico=data['correo_electronico'])
            empresa.save()
            return render(request, 'inicio.html', {})

    form=empresa_formulario
    return render(request, "registro/registro-bloggeros.html",{'form':form})





def busqueda(request):
    return render(request, "busqueda/busqueda.html", {})

def lista_lectores(request):
    nombre_anonimo_a_buscar=request.GET.get('nombre_anonimo', None)

    if nombre_anonimo_a_buscar is not None:
        lectores=Lector.objects.filter(nombre_anonimo__icontains=nombre_anonimo_a_buscar)
    else:
        lectores= Lector.objects.all()
    
    form=lector_busqueda()
    return render(request, "busqueda/lista-lectores.html",{'form':form, 'lectores':lectores})

def lista_bloggeros(request):
    alias_a_buscar=request.GET.get('alias', None)

    if alias_a_buscar is not None:
        bloggeros=Bloggero.objects.filter(alias__icontains=alias_a_buscar)
    else:
        bloggeros=Bloggero.objects.all()
    
    form=bloggero_busqueda()
    return render(request, "busqueda/lista-bloggeros.html",{'form':form, 'bloggeros':bloggeros})

def lista_empresas(request):
    nombre_de_empresa_a_buscar=request.GET.get('nombre_de_empresa', None)

    if nombre_de_empresa_a_buscar is not None:
        empresas=Empresa.objects.filter(alias__icontains=nombre_de_empresa_a_buscar)
    else:
        empresas=Empresa.objects.all()
    
    form=empresa_busqueda()
    return render(request, "busqueda/lista-empresas.html",{'form':form, 'empresas':empresas})