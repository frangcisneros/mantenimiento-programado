from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views

# Importa tus ViewSets desde views/api.py
from .views.api import (
    MaquinaViewSet,
    PiezaViewSet,
    EncargadoViewSet,
    MantenimientoViewSet,
    TareaViewSet,
    PiezasUtilizadasViewSet,
)

# Importa tus vistas de plantilla desde views/web.py
from .views.web import (
    panel_control,
    crear_mantenimiento,
    crear_maquina_1,
    crear_maquina_2,
    crear_tarea,
    ver_inventario,
    ver_mantenimiento,
    ver_maquina_1,
    ver_maquina_2,
    ver_tareas,
    crear_maquina,
    listar_maquinas,
    crear_tipo_mantenimiento,
    crear_intervalo,
    crear_encargado,
    admin_panel,
    crear_tipo_maquina,
    registrar_usuario,
    verificar_codigo,
    ver_tarea_detalle,
    ver_maquinas,
    ver_planes,
)

router = DefaultRouter()
router.register(r"maquinas", MaquinaViewSet)
router.register(r"piezas", PiezaViewSet)
router.register(r"encargados", EncargadoViewSet)
router.register(r"mantenimientos", MantenimientoViewSet)
router.register(r"tareas", TareaViewSet)
router.register(r"piezas_utilizadas", PiezasUtilizadasViewSet)

urlpatterns = [
    # ——— RUTAS DE LA API ——————————————————————————————————
    # List/Create/Update/Delete de tus modelos
    path("api/", include(router.urls)),
    # Ruta extra para el APIView de usar pieza
    # ——— RUTAS DE LA INTERFAZ WEB —————————————————————————
    path("panel-control/", panel_control, name="panel-control"),
    path(
        "crear-tipo-mantenimiento/",
        crear_tipo_mantenimiento,
        name="crear-tipo-mantenimiento",
    ),
    path("crear-intervalo/", crear_intervalo, name="crear-intervalo"),
    path("crear-mantenimiento/", crear_mantenimiento, name="crear-mantenimiento"),
    path("crear-maquina-1/", crear_maquina_1, name="crear-maquina_1"),
    path("crear-maquina/", crear_maquina, name="crear_maquina"),
    path("crear-tipo-maquina/", crear_tipo_maquina, name="crear-tipo-maquina"),
    path("crear-maquina-2/", crear_maquina_2, name="crear-maquina_2"),
    path("crear-tarea/", crear_tarea, name="crear-tarea"),
    path("ver-inventario/", ver_inventario, name="ver-inventario"),
    path("ver-mantenimiento/", ver_mantenimiento, name="ver-mantenimiento"),
    path("ver-maquina-2/", ver_maquina_2, name="ver-maquinas-2"),
    path(
        "ver-tarea-detalle/<int:id_tarea>/", ver_tarea_detalle, name="ver-tarea-detalle"
    ),
    path("crear-encargado/", crear_encargado, name="crear-encargado"),
    path("admin-panel/", admin_panel, name="admin-panel"),
    path("verificar-codigo/", verificar_codigo, name="verificar-codigo"),
    path("register/", registrar_usuario, name="register"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # nuevas rutas
    path("ver-maquinas/", ver_maquinas, name="ver-maquinas"),
    path("ver-planes/", ver_planes, name="ver-planes"),
    path("ver-tareas/", ver_tareas, name="ver-tareas"),

]
