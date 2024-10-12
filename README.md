# Proyecto Nube Miso

Este proyecto es una aplicación de backend construida con FastAPI y Celery, que permite la carga y procesamiento de archivos de video. Utiliza Redis como broker de tareas para Celery.



## Tecnologías Utilizadas

- **FastAPI**: Un marco web moderno y rápido para construir APIs con Python.
- **Celery**: Un framework para el manejo de tareas asíncronas.
- **Redis**: Un almacén de datos en memoria, utilizado como broker de tareas.
- **MoviePy**: Una biblioteca para la edición de videos en Python.

## Estructura del Proyecto

```plaintext
nube-miso/
├── backend/
│   ├── app/
│   │   ├── main.py           # Archivo principal de la aplicación FastAPI
│   │   └── tasks.py          # Definición de tareas de Celery
│   └── Dockerfile             # Dockerfile para construir la imagen del backend
├── worker/
│   ├── worker.py             # Archivo principal del worker de Celery
│   └── Dockerfile             # Dockerfile para construir la imagen del worker
├── processed_audios/          # Carpeta para almacenar audios procesados
├── videos/                    # Carpeta para almacenar videos subidos
├── requirements.txt           # Dependencias del proyecto
└── docker-compose.yml         # Configuración de Docker Compose
```

## Configuración del Entorno
Clona el repositorio:

git clone https://github.com/miguelenruiz1/nube-miso.git
cd nube-miso

## Crea un entorno virtual y actívalo:
```
python -m venv venv
.\venv\Scripts\activate  # En Windows 
```
## Instala las dependencias:
```
pip install -r requirements.txt
 ```
## Configuración de Docker

```
docker-compose up --build 
```

## Contenedores
### Backend:

- Descripción: Este contenedor ejecuta la aplicación FastAPI que maneja las solicitudes de la API.
- Puerto: 8000
- Comando:
 ```
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
 ```
### worker:

- Descripción: Este contenedor ejecuta el worker de Celery, que procesa las tareas en segundo plano, como la extracción de audio de los videos subidos.
```
celery -A tasks worker --loglevel=info
```
## redis:

- Descripción: Este contenedor proporciona el servicio de Redis, que actúa como broker para las tareas de Celery.
Puerto: 6379


## Uso de la API

- Abre Postman.
- Selecciona el método POST.
- Ingresa la URL: http://127.0.0.1:8000/upload.
- En la sección "Body", selecciona form-data.
- Agrega un campo con la clave file y selecciona un archivo de video.
- Envía la solicitud.

## Logs y Tareas
Los logs de la aplicación y del worker de Celery se pueden ver con el siguiente comando:
```
docker-compose logs -f
```



