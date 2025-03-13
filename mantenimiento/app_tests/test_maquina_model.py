from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from mantenimiento.models import Maquina
from mantenimiento.repositories import MaquinaRepository


class MaquinaModelTestCase(APITestCase):
    def setUp(self):
        self.maquina_test = Maquina(nombre="Máquina 1", descripcion="Descripción 1")
        self.maquina_repository = MaquinaRepository()

    def test_maquina_save(self):
        self.maquina_repository.save(self.maquina_test)
        # TODO: crear un metodo para buscar por id
        maquina = Maquina.objects.get(nombre="Máquina 1")
        assert maquina.nombre == "Máquina 1"
