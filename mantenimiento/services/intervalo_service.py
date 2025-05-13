from ..models import OpcionesIntervalo


class IntervaloService:
    def obtener_intervalos(self):
        # Devuelve directamente el queryset completo
        return OpcionesIntervalo.objects.all()
