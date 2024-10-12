import os
import logging
from fastapi import FastAPI, UploadFile, File
from celery import Celery

# Configuración del logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Asegura que la carpeta de videos existe
os.makedirs("videos", exist_ok=True)

# Configura Celery
celery_app = Celery('tasks', broker='redis://redis:6379/0')

@app.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    try:
        file_location = f"videos/{file.filename}"
        
        # Guardar el archivo subido
        with open(file_location, "wb") as f:
            f.write(await file.read())
            
        # Registra información sobre el archivo recibido
        logger.info(f"Received video file: {file.filename}")
        logger.info(f"Saved video to: {file_location}")
        
        # Envía la tarea al worker
        celery_app.send_task('tasks.process_video', args=[file.filename])
        
        return {"message": "Video uploaded and processing started", "filename": file.filename}
    
    except Exception as e:
        logger.error(f"Error while uploading video: {str(e)}")
        return {"error": str(e)}, 500


