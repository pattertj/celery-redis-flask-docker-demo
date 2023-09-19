"""The main Flask API."""

import os

from bleach import clean
from dotenv import load_dotenv
from flask import Flask, Response, jsonify, make_response
from redbeat import RedBeatSchedulerEntry as Entry
from redis import Redis

import tasks.tasks as t

load_dotenv()

REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_HOST = os.getenv("REDIS_HOST", "redis")

FLASK_RUN_PORT = int(os.getenv("FLASK_RUN_PORT", 8000))
FLASK_RUN_HOST = os.getenv("FLASK_RUN_HOST", "127.0.0.1")

app = Flask(__name__)
redis = Redis(host=REDIS_HOST, port=REDIS_PORT)


@app.route("/")
def hello() -> Response:
    """Start a new task."""
    counter = redis.incr("hits")

    # Run a task named task{counter} every .5 second and save it.
    entry = Entry(
        f"task{counter}", "app.tasks.tasks.my_background_task", 0.5, app=t.app
    )
    entry.save()
    return make_response(f"This webpage has been viewed {counter} time(s)", 200)


@app.route("/stop/<id>")
def goodbye(id: str):
    """Stop a given task ID.

    Args:
        id (str): Task ID
    """
    clean_id = clean(id)

    try:
        e = Entry.from_key(f"redbeat:task{clean_id}", app=t.app)
        e.delete()
    except KeyError as e:
        response = {"error": f"KeyError: {str(e)}"}
        return make_response(jsonify(response), 500)

    return make_response(f"Task task{clean_id} has been deleted.", 200)


if __name__ == "__main__":
    app.run(host=FLASK_RUN_HOST, port=FLASK_RUN_PORT)
