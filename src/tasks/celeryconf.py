"""Celery config file."""
import os

from dotenv import load_dotenv

load_dotenv()

REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_HOST = os.getenv("REDIS_HOST", "redis")

redbeat_redis_url = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
broker_url = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
result_backend = f"redis://{REDIS_HOST}:{REDIS_PORT}/1"

beat_scheduler = "redbeat.RedBeatScheduler"
beat_max_loop_interval = (
    5  # This is short and may cause perf/scale/latency/load issues in prod.
)
beat_schedule: dict = {}
