import time
import uuid
from .celery import app

@app.task
def ping():
    return 1

@app.task
def now():
    return time.time()

@app.task
def id():
    return str(uuid.uuid4())
