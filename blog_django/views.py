from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def inicio(request):
    return render(request, "inicio.html", {})

def registro(request):
    return render(request, "registro.html", {})