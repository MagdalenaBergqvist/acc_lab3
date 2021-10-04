from flask import Flask
import tasks
import json
app = Flask(__name__)
@app.route('/')
def welcolme():
    r = tasks.func.delay()
    return json.dumps(r.wait(), indent=4)
if __name__ == '__main__':
    app.run(host='0.0.0.0')#, port=5000)
