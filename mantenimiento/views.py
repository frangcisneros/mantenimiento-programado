from django.shortcuts import render
from django.http import HttpResponse
from .models import Maquina, TareaMantenimiento


def index(request):
    return render(request, "mantenimiento/index.html")


def lista_maquinas(request):
    maquinas = Maquina.objects.all()
    return render(request, "mantenimiento/lista_maquinas.html", {"maquinas": maquinas})


def formulario_creacion_maquina(request):
    return render(request, "mantenimiento/formulario_creacion_maquina.html")


def lista_tareas(request):
    tareas = TareaMantenimiento.objects.all()
    return render(request, "mantenimiento/lista_tareas.html", {"tareas": tareas})


def formulario_creacion_tarea(request):
    return render(request, "mantenimiento/formulario_creacion_tarea.html")
