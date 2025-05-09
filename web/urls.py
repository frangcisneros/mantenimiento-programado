from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import registrar_usuario

urlpatterns = [
    path("register/", registrar_usuario, name="register"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("panel-control/", views.panel_control, name="panel-control"),
    path("crear-mantenimiento/", views.crear_mantenimiento, name="crear-mantenimiento"),
    path("crear-maquina-1/", views.crear_maquina_1, name="crear-maquina_1"),
    path("crear-maquina-2/", views.crear_maquina_2, name="crear-maquina_2"),
    path("crear-tarea/", views.crear_tarea, name="crear-tarea"),
    path("ver-inventario/", views.ver_inventario, name="ver-inventario"),
    path("ver-mantenimiento/", views.ver_mantenimiento, name="ver-mantenimiento"),
    path("ver-maquinas-1/", views.ver_maquina_1, name="ver-maquinas-1"),
    path("ver-maquina-2/", views.ver_maquina_2, name="ver-maquina-2"),
    path("ver-tarea/", views.ver_tarea, name="ver-tarea"),
]
