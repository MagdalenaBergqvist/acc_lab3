from celery import Celery
from extract import count_pronouns

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

@app.task
def func():
    print("tasks")
    return count_pronouns()
