FROM python:3.13.4-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Copia el archivo de requerimientos e instala dependencias
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto del proyecto
COPY . /app/

# Expone el puerto donde Gunicorn atenderá
EXPOSE 8000

# Comando para arrancar Gunicorn (ajusta la ruta al WSGI de tu proyecto)
CMD ["gunicorn", "main_app.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
