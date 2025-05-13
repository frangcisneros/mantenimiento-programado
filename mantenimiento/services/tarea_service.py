from ..models import Tarea


class TareaService:
    def obtener_tareas(self):
        # Devuelve directamente el queryset completo
        return Tarea.objects.all()
