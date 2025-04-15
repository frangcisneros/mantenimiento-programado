from django.urls import path
from . import views

urlpatterns = [
    path("panel_control/", views.panel_control, name="panel_control"),
    path("crear-mantenimiento/", views.crear_mantenimiento, name="crear_mantenimiento"),
    path("crear-maquina-1/", views.crear_maquina_1, name="crear_maquina_1"),
    path("crear-maquina-2/", views.crear_maquina_2, name="crear_maquina_2"),
    path("crear-tarea/", views.crear_tarea, name="crear_tarea"),
    path("ver-inventario/", views.ver_inventario, name="ver_inventario"),
    path("ver-mantenimiento/", views.ver_mantenimiento, name="ver_mantenimiento"),
    path("ver-maquina-1/", views.ver_maquina_1, name="ver_maquina_1"),
    path("ver-maquina-2/", views.ver_maquina_2, name="ver_maquina_2"),
    path("ver-tarea/", views.ver_tarea, name="ver_tarea"),
]
