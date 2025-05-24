from ..models import Mantenimiento, OpcionesMantenimiento


class MantenimientoService:
    def obtener_mantenimientos(self):
        # Devuelve directamente el queryset completo
        return Mantenimiento.objects.all()

    def obtener_tipos_mantenimiento(self):
        # Devuelve directamente el queryset completo
        return OpcionesMantenimiento.objects.all()
    
    def obtener_mantenimiento_por_id(self, id_mantenimiento):
        # Devuelve el mantenimiento con el id especificado
        return Mantenimiento.objects.get(id_mantenimiento=id_mantenimiento)
