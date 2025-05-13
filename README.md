# To-Do

- [ ] Poder cargarle el plan de mantenimiento a una maquina.
- [ x ] Repuestos enlazados a maquinas y tareas.
- [ ] Arreglar modelo de mantenimiento, faltaria tambien la "maquina"

# To-Do Interfaz

- [ x ] Iconos en los botones del panel de control
- [ x ] Que se resalte en la navbar cuando estoy en una de esas páginas
- [ x ] Que se resalten los botones del panel de control cuando paso el mouse
- [ x ] Botones tamaño dinamico

# Material de referencia para manuales

https://www.aslak.es/pub/media/fichas_tecnicas/3420260.pdf

# Comandos

docker system prune -a -f

docker-compose up --build -d

python manage.py makemigrations

python manage.py migrate api

pip freeze > requirements.txt

python manage.py runserver

Para crear grupos

python manage.py create_groups
