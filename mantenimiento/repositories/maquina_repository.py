from mantenimiento.models import Maquina


class MaquinaRepository:
    @staticmethod
    def save(maquina: Maquina):
        maquina.save()

    @staticmethod
    def delete(maquina: Maquina):
        maquina.delete()
