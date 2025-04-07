# ACA ES DONDE SE VAN A MANEJAR LOS REPOSITORIOS

from .models import TipoMantenimiento, Encargado, Maquina, Pieza, TareaMantenimiento


class MaquinaRepo:
    def save(self, maquina: Maquina):
        maquina.save()
        return maquina

    def delete(self, maquina: Maquina):
        maquina.delete()
        return maquina

    def find_by_id(self, id: int):
        try:
            return Maquina.objects.get(id_maquina=id)
        except Maquina.DoesNotExist:
            return None

    def find_all(self):
        return Maquina.objects.all()
