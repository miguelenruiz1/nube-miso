import os
import logging
from celery import Celery
import moviepy.editor as mp

# Configura el logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configura Celery
celery_app = Celery('tasks', broker='redis://redis:6379/0')

@celery_app.task(name='tasks.process_video')
def process_video(filename):
    video_path = f"videos/{filename}"
    output_path = f"processed_audios/{filename.split('.')[0]}.mp3"
    
    logger.info(f"Starting to process video: {video_path}")
    
    # Verifica si el archivo de video existe
    if not os.path.exists(video_path):
        logger.error(f"Video file does not exist: {video_path}")
        return {"error": "Video file not found"}
    
    try:
        # Procesa el video y extrae el audio
        video = mp.VideoFileClip(video_path)
        video.audio.write_audiofile(output_path)
        logger.info(f"Successfully processed video: {video_path} to {output_path}")
    except Exception as e:
        logger.error(f"Error processing video {video_path}: {e}")
        return {"error": str(e)}
    
    return {"message": "Video processed successfully", "output_file": output_path}
