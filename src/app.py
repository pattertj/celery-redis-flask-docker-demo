# import json
# import random
from flask import Flask
from redbeat import RedBeatSchedulerEntry as Entry
from redis import Redis

import tasks.tasks as t

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello():
    redis.incr('hits')
    counter = str(redis.get('hits'), 'utf-8')

    entry = Entry(f'task{counter}', 'app.tasks.tasks.my_background_task', .1, app=t.app)
    entry.save()

    return f"This webpage has been viewed {counter} time(s)"


@app.route('/stop/<id>')
def goodbye(id: int):
    e = Entry.from_key(f'redbeat:task{id}', app=t.app)
    e.delete()

    return f"Task task{id} has been deleted."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
