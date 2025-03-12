from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Maquina, TareaMantenimiento
from .serializers import MaquinaSerializer


@api_view(["GET"])
def lista_maquinas_api(request):
    maquinas = Maquina.objects.all()
    serializer = MaquinaSerializer(maquinas, many=True)
    return Response(serializer.data)


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
