# To-Do

- [ ] Poder cargarle el plan de mantenimiento a una maquina.
- [ ] Interfaz bonita.
- [ x ] Repuestos enlazados a maquinas y tareas.
- [ ] Arreglar modelo de mantenimiento, faltaria tambien la "maquina"

# Material de referencia para manuales

https://www.aslak.es/pub/media/fichas_tecnicas/3420260.pdf

# Comandos

docker system prune -a -f

docker-compose up --build -d

python manage.py makemigrations

python manage.py migrate api

pip freeze > requirements.txt
