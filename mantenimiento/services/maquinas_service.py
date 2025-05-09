from ..models import Maquina, OpcionesMaquina


class MaquinasService:
    def crear_maquina(self, tipo_maquina):
        # * crea una nueva maquina
        # * primero comprueba que el tipo de maquina sea valido
        self.comprobar_tipo_maquina(tipo_maquina)
        # * luego crea la maquina
        maquina = Maquina(tipo_maquina=tipo_maquina)
        maquina.save()

    # * metodo para comprobar que el tipo de maquina sea de la tablas de tipo maquina probablemente deberia sacarlo de aca
    def comprobar_tipo_maquina(self, tipo_maquina):
        # * comprueba que el tipo de maquina sea de la tablas de tipo maquina
        if not OpcionesMaquina.objects.filter(tipo_maquina=tipo_maquina).exists():
            raise ValueError("El tipo de maquina no es valido")
