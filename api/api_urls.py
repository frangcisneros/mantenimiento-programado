from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UsarPiezaAPIView
from .views import (
    MaquinaViewSet,
    PiezaViewSet,
    EncargadoViewSet,
    MantenimientoViewSet,
    TareaViewSet,
    PiezasUtilizadasViewSet,
)

router = DefaultRouter()
router.register(r"maquinas", MaquinaViewSet)
router.register(r"piezas", PiezaViewSet)
router.register(r"encargados", EncargadoViewSet)
router.register(r"mantenimientos", MantenimientoViewSet)
router.register(r"tareas", TareaViewSet)
router.register(r"piezas_utilizadas", PiezasUtilizadasViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("usar-pieza/", UsarPiezaAPIView.as_view(), name="usar-pieza"),
]
