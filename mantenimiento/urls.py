from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Importa tus ViewSets desde views/api.py
from .views.api import (
    MaquinaViewSet,
    PiezaViewSet,
    EncargadoViewSet,
    MantenimientoViewSet,
    TareaViewSet,
    PiezasUtilizadasViewSet,
    UsarPiezaAPIView,
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
    ver_tarea,
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
    path("api/usar-pieza/", UsarPiezaAPIView.as_view(), name="api-usar-pieza"),
    # ——— RUTAS DE LA INTERFAZ WEB —————————————————————————
    path("panel-control/", panel_control, name="panel-control"),
    path("crear-mantenimiento/", crear_mantenimiento, name="crear-mantenimiento"),
    path("crear-maquina-1/", crear_maquina_1, name="crear-maquina_1"),
    path("crear-maquina-2/", crear_maquina_2, name="crear-maquina_2"),
    path("crear-tarea/", crear_tarea, name="crear-tarea"),
    path("ver-inventario/", ver_inventario, name="ver-inventario"),
    path("ver-mantenimiento/", ver_mantenimiento, name="ver-mantenimiento"),
    path("ver-maquina-1/", ver_maquina_1, name="ver-maquinas-1"),
    path("ver-maquina-2/", ver_maquina_2, name="ver-maquinas-2"),
    path("ver-tarea/", ver_tarea, name="ver-tarea"),
]
