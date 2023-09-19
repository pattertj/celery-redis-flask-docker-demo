"""Task module containing the task logic."""
import os
from time import sleep

from celery import Celery
from dotenv import load_dotenv
from redis import Redis

from . import celeryconf

load_dotenv()

REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_HOST = os.getenv("REDIS_HOST", "redis")

# Initialize Celery
app: Celery = Celery("tasks")
app.config_from_object(celeryconf)

# Initialize Redis
redis = Redis(host=REDIS_HOST, port=REDIS_PORT)


# Define a sample Celery task
@app.task
def my_background_task():
    """Run the sample background task."""
    sleep(2)
    redis.incr("background-count")
