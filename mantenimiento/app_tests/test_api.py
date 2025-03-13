from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from mantenimiento.models import Maquina


class MaquinaAPITestCase(APITestCase):
    def setUp(self):
        # Creamos algunas instancias de Maquina para nuestros tests
        Maquina.objects.create(nombre="Máquina 1", descripcion="Descripción 1")
        Maquina.objects.create(nombre="Máquina 2", descripcion="Descripción 2")

    def test_lista_maquinas(self):
        url = reverse("lista_maquinas_api")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Comprobamos que se devuelven las dos máquinas que hemos creado
        self.assertEqual(len(response.json()), 2)
