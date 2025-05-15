**Aplicación Web para Control de Mantenimiento de Máquinas**

**Descripción**

Aplicación Web para llevar un control del mantenimiento de las máquinas dentro de una empresa. Permite registrar tipos de máquinas, planificar y ejecutar tareas de mantenimiento, gestionar piezas e inventarios, asignar encargados y llevar un historial completo de cada actividad.

**Características principales**

- **Gestión de Máquinas**: creación, edición y listado de máquinas según opciones configurables.
- **Catálogo de Piezas**: control de inventario de piezas con tipos dinámicos y cantidades.
- **Mantenimientos**: definición de tipos e intervalos de mantenimiento (semanal, mensual, etc.) con instrucciones detalladas.
- **Tareas de Mantenimiento**: asignación de mantenimientos a máquinas y encargados; registro de inicio y fin de la tarea.
- **Piezas Utilizadas**: generación automática de registros de piezas usadas en cada tarea, con ajuste de stock.
- **API RESTful**: endpoints para todos los modelos (Máquina, Pieza, Mantenimiento, Tarea, Encargado, Piezas Utilizadas) construidos con Django REST Framework.
- **Interfaz Web**: panel de control con navegación por roles (administrador vs. operador), formularios dinámicos y plantillas en Django.
- **Autenticación y Roles**: sistema de usuarios con roles diferenciados para mostrar/ocultar funcionalidades según permisos.
- **Dockerizado**: despliegue de entornos de desarrollo y producción con contenedores separados para la aplicación y la base de datos PostgreSQL.
- **Separación de Configuraciones**: settings modularizados (base, development, production) para gestionar distintas bases de datos y parámetros.
- **Buenas Prácticas**: arquitectura en capas (repositorios, servicios), tests con Django TestCase, uso de ModelForms y validación automática.

**Tecnologías**

- **Backend**: Python 3.13, Django 5.x, Django REST Framework
- **Base de Datos**: PostgreSQL
- **Frontend**: HTML5, Bootstrap 5, JavaScript (Fetch API)
- **Contenerización**: Docker, docker-compose

**Instalación y Ejecución**

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/mantenimiento-programado.git
   cd mantenimiento-programado
   ```

2. Copia el ejemplo de variables de entorno y ajusta credenciales:

   ```bash
   cp .env.example .env
   # Edita .env con tu DB_USER, DB_PASSWORD, etc.
   ```

3. Levanta los contenedores:

   ```bash
   docker-compose up --build
   ```

4. Ejecuta migraciones y crea superusuario:

   ```bash
   docker-compose exec web_staging python manage.py migrate
   docker-compose exec web_staging python manage.py createsuperuser
   ```

5. Accede en tu navegador:

   - Panel de control: [http://localhost:8000/panel-control/](http://localhost:8000/panel-control/)
   - API browsable: [http://localhost:8000/api/](http://localhost:8000/api/)

**Uso**

- Registra opciones de máquina, intervalo y tipos de mantenimiento desde el admin de Django.
- Crea máquinas y planifica tareas desde el panel de control.
- Monitorea inventario y piezas desde la interfaz web.
- Consume la API desde cualquier cliente HTTP para integración externa.

# Material de referencia para manuales

https://www.aslak.es/pub/media/fichas_tecnicas/3420260.pdf

# Comandos utiles

docker system prune -a -f

docker-compose up --build -d

python manage.py makemigrations

python manage.py migrate api

pip freeze > requirements.txt

python manage.py runserver

Para crear grupos

python manage.py create_groups
