from django.core.exceptions import ObjectDoesNotExist
from ..models import Maquina, OpcionesMaquina


class MaquinasService:
    def obtener_maquinas(self):
        """
        Muestra todas las máquinas registradas en la base de datos.
        """
        return Maquina.objects.all()
    
    def obtener_maquina_por_id(self, id_maquina):
        """
        Muestra una máquina específica según su ID.
        """
        try:
            return Maquina.objects.get(id_maquina=id_maquina)
        except ObjectDoesNotExist:
            return None
