from ..models import Encargado


class EncargadoService:
    def obtener_encargados(self):
        # Devuelve directamente el queryset completo
        return Encargado.objects.all()
