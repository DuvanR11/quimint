from ast import Try
from django.http import HttpResponseRedirect
from urllib.request import Request
from django.shortcuts import render, redirect

from principal.models import Equipos
from .forms import *
from django.contrib.messages import constants as messages
from django.contrib import messages

# Create your views here.

# Session Principal de la pagina
def principal(request):
    return render(request, 'pages/principal.html')


# CRUD de equipos
'''
Funcion para agregar equipos y retorno de mensajes
'''
def agregarEquipos(request):
    equipos = Equipos.objects.all()
    form = formEquipos(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Por fin")
        return HttpResponseRedirect('/')
    else:
        messages.error(request, "error")
    data={
        'form': form,
        'equipos':equipos
    }
    return render(request, 'pages/equipos.html',data)


# '''
# Funcion Mostrar solo un equipo
# '''
def mostrarEquipo(request, id):
    equipo = Equipos.objects.get(id=id)
    data={
        'equipo':equipo
    }
    return render(request, 'pages/equipo.html',data)

# '''
# Funcion Eliminar equipo
# '''
# def eliminarEquipo(request, id):
#     equipos = Equipos.objects.get(id=id)
#     equipos.delete()
#     data={
#         'equipos':equipos
#     }
#     return render(request, 'pages/equipo.html',data)

# '''
# Funcion Eliminar equipo
# '''
# def actualizarEquipo(request, id):
#     equipo = Equipos.objects.get(id=id)
#     if request.method == 'GET':
#         form = Equipos(instance = equipo)
#         data ={
#            'form': form,
#            'id': id
#         }
#         return render(request, 'pages/equipo.html',data)
    
#     if request.method == 'POST':
#         form = Equipos(request.POST, instance = equipo)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Envio exitoso')
#         else:
#             messages.warning(request, 'Error')
#         return HTTPResponse(Request.POST)

# CRUD de Suministros
'''
Funcion para agregar equipos y retorno de mensajes
'''
def agregarSuministros(request):
    suministros = Suministros.objects.all()
    form = formSuministros(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Por fin")
        return HttpResponseRedirect('/')
    else:
        messages.error(request, "error")
    data={
        'form': form,
        'suministros':suministros
    }
    return render(request, 'pages/suministros.html',data)


# '''
# Funcion Mostrar solo un equipo
# '''
def mostrarSuministros(request, id):
    suministros = Suministros.objects.get(id=id)
    data={
        'suministros':suministros
    }
    return render(request, 'pages/suministros.html',data)


# CRUD de Herramientas
'''
Funcion para agregar equipos y retorno de mensajes
'''
def agregarHerramientas(request):
    herramientas = Herramientas.objects.all()
    form = formHerramientas(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Por fin")
        return HttpResponseRedirect('/')
    else:
        messages.error(request, "error")
    data={
        'form': form,
        'herramientas':herramientas
    }
    return render(request, 'pages/herramientas.html',data)



# '''
# Funcion Mostrar solo un equipo
# '''
def mostrarHerramientas(request, id):
    herramientas = Herramientas.objects.get(id=id)
    data={
        'herramientas':herramientas
    }
    return render(request, 'pages/herramientas.html',data)