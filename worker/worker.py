from celery import Celery
from kafka import KafkaConsumer
from app.tasks import process_video

# Configura la aplicación Celery
app = Celery('worker', broker='redis://redis:6379/0')

# Configura el consumidor Kafka
consumer = KafkaConsumer(
    'nombre_del_tema',
    bootstrap_servers=['broker:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='grupo_worker'
)

# Tarea ejemplo en Celery
@app.task
def procesar_mensaje_kafka(mensaje):
    print(f"Procesando mensaje: {mensaje}")

# Ejemplo de ejecución en bucle
for mensaje in consumer:
    procesar_mensaje_kafka.delay(mensaje.value.decode('utf-8'))
