from rest_framework.routers import DefaultRouter
from .views import (
    MaquinaViewSet,
    TareaMantenimientoViewSet,
    PiezaViewSet,
    TipoMantenimientoViewSet,
    EncargadoViewSet,
)

router = DefaultRouter()
router.register(r"maquinas", MaquinaViewSet)
router.register(r"tareas", TareaMantenimientoViewSet)
router.register(r"pieza", PiezaViewSet)
router.register(r"tipos", TipoMantenimientoViewSet)
router.register(r"encargados", EncargadoViewSet)

urlpatterns = router.urls
