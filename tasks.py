from celery import Celery
from extract import count_pronouns

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def func():
    count_pronouns()
