from flask import Flask
import tasks
app = Flask(__name__)
@app.route('/')
def welcolme():
    r = tasks.func.delay()
    return r.wait()
    #return "Hello World!"
if __name__ == '__main__':
    app.run(host='0.0.0.0')#, port=5000)
