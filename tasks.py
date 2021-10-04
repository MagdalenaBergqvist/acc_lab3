from celery import Celery
from extract import count_pronouns

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y
