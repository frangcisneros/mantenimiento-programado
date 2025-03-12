# Usa una imagen base de Python 
FROM python:3.13.2-slim


# Evita la creación de archivos .pyc y asegura que la salida de logs se muestre en tiempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos y instala las dependencias
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto de tu proyecto al directorio de trabajo
COPY . /app/

# Expone el puerto en el que correrá Django (por defecto 8000)
EXPOSE 8000

# Define el comando que ejecutará el servidor de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
