from ..models import Mantenimiento, OpcionesMantenimiento


class MantenimientoService:
    def obtener_mantenimientos(self):
        # Devuelve directamente el queryset completo
        return Mantenimiento.objects.all()

    def obtener_tipos_mantenimiento(self):
        # Devuelve directamente el queryset completo
        return OpcionesMantenimiento.objects.all()
