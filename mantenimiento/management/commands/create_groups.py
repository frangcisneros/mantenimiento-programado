from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = "Crea el grupo 'Jefes de Área' con permisos específicos"

    def handle(self, *args, **kwargs):
        # Crear el grupo
        group, created = Group.objects.get_or_create(name="Jefes de Área")

        # Asignar permisos al grupo (opcional)
        # Ejemplo: permiso para acceder a una vista específica
        permisos = Permission.objects.filter(
            codename__in=["add_maquina", "change_maquina"]
        )
        group.permissions.set(permisos)

        self.stdout.write(self.style.SUCCESS("Grupo 'Jefes de Área' creado con éxito."))
