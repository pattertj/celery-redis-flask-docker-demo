from time import sleep
from celery import Celery
from redis import Redis
from . import celeryconf

# Initialize Celery
app: Celery = Celery('tasks')
app.config_from_object(celeryconf)

# Initialize Redis
redis = Redis(host='redis', port=6379)


# Define a sample Celery task
@app.task
def my_background_task():
    sleep(2)
    redis.incr('background-count')
