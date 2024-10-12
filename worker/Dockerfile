# Dockerfile para el worker
FROM python:3.9-slim

WORKDIR /app

# Copia el archivo de requisitos
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente del worker
COPY worker.py /app/

# Comando para iniciar el worker de Celery
CMD ["celery", "-A", "app.tasks", "worker", "--loglevel=info"]
