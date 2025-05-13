from ..models import OpcionesMaquina


class TipoMaquinaService:
    def obtener_tipos_maquina(self):
        # Devuelve directamente el queryset completo
        return OpcionesMaquina.objects.all()
