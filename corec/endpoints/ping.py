import time
import uuid
from .celery import app

@app.task
def ping():
    print(app.conf)
    return 1

@app.task
def now():
    return time.time()

@app.task
def id():
    return str(uuid.uuid4())
