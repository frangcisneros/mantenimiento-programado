from ..models import Tarea


class TareaService:
    def obtener_tareas(self):
        # Devuelve directamente el queryset completo
        return Tarea.objects.all()

    def obtener_tarea_por_id(self, id_tarea):
        # Devuelve la tarea con el ID especificado
        try:
            return Tarea.objects.get(id_tarea=id_tarea)
        except Tarea.DoesNotExist:
            return None
