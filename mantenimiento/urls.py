from django.urls import path
from . import views
from .views import lista_maquinas_api

urlpatterns = [
    path("", views.index, name="index"),
    path("maquinas/", views.lista_maquinas, name="lista_maquinas"),
    path("tareas/", views.lista_tareas, name="lista_tareas"),
    path(
        "formulario-creacion-maquina/",
        views.formulario_creacion_maquina,
        name="formulario_creacion_maquina",
    ),
    path(
        "formulario-creacion-tarea/",
        views.formulario_creacion_tarea,
        name="formulario_creacion_tarea",
    ),
    path("api/maquinas/", lista_maquinas_api, name="lista_maquinas_api"),
]
