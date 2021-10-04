from celery import Celery
from extract import count_pronouns

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')
print("eogrb")
@app.task
def func():
    return count_pronouns()
