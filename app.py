from flask import Flask
import tasks
app = Flask(__name__)
@app.route('/')
def welcolme():
    print("1")
    r = tasks.func.delay()
    print("2")
    return r.wait()
    #return "Hello World!"
if __name__ == '__main__':
    app.run(host='0.0.0.0')#, port=5000)
