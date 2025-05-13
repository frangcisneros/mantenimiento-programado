from ..models import Pieza, PiezasUtilizadas


class PiezasService:
    # * mueve desde la tabla Pieza a la tabla PiezasUtilizadas
    def usar_pieza(self, id_pieza, cantidad, id_tarea):
        pieza = Pieza.objects.get(id_pieza=id_pieza)
        # * si la cantidad de piezas es mayor a la cantidad de piezas disponibles, no se puede usar la pieza
        if pieza.cantidad < cantidad:
            raise ValueError("No hay suficientes piezas disponibles")
        pieza.cantidad -= cantidad
        pieza.save()
        # * se crea la pieza utilizada
        piezas_utilizadas = PiezasUtilizadas(
            pieza=pieza, id_tarea_id=id_tarea, cantidad=cantidad
        )
        piezas_utilizadas.save()
