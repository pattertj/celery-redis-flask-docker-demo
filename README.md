# celery-redis-flask-docker-demo

This is a sample project on how to organize, build, and deploy Celery, Beat, Flower, Redis, and Flask on Docker.

To go, simply run:

```bash
docker-compose up --build
```

- The primary endpoint will be on http://localhost:8000. Go here to start tasks processing.
- Flower will be on http://localhost:5555 to monitor task progress.
