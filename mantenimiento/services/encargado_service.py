from ..models import Encargado


class EncargadoService:
    def obtener_encargados(self):
        # Devuelve directamente el queryset completo
        return Encargado.objects.all()
    
    def obtener_encargado_por_id(self, id_encargado):
        # Devuelve el encargado con el id especificado
        return Encargado.objects.get(id_encargado=id_encargado)
