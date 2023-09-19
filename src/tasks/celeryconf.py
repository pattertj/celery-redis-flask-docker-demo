redbeat_redis_url = "redis://redis:6379/0"
broker_url = "redis://redis:6379/0"
result_backend = "redis://redis:6379/1"

beat_scheduler = 'redbeat.RedBeatScheduler'
beat_max_loop_interval = 5
beat_schedule: dict = {}
