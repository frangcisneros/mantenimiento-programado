from ..models import Mantenimiento


class MantenimientoService:
    def obtener_mantenimientos(self):
        # Devuelve directamente el queryset completo
        return Mantenimiento.objects.all()
