# mantenimiento-programado

docker system prune -a -f

docker-compose up --build -d

python manage.py makemigrations

python manage.py migrate api

pip freeze > requirements.txt
