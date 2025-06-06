from django.core.exceptions import ObjectDoesNotExist
from ..models import Maquina, OpcionesMaquina


class MaquinasService:
    def obtener_maquinas(self):
        """
        Muestra todas las máquinas registradas en la base de datos.
        """
        return Maquina.objects.all()
