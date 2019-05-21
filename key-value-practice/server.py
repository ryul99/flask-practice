import time, json, signal
from flask import Flask, request
d = dict()
app = Flask(__name__)
try:
    with open("record.txt", 'r') as fr:
        d = json.loads(fr.readline())
except:
    ''


def signal_handler(signal, frame):
    with open("record.txt", 'w') as fw:
        fw.write(json.dumps(d))
    quit()
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


@app.route('/GET', methods = ['GET'])
def get():
    j = request.json
    key = j['key']
    if key in d and (d[key][1] == -1 or time.time() < d[key][1]):
        return d[key][0]
    if key in d :
        del d[key]
    return ''


@app.route('/SET', methods = ['POST'])
def set():
    j = request.json
    key = j['key']
    value = j['value']
    d[key] = [value, -1]
    return value


@app.route('/EXPIRE', methods = ['POST'])
def expire():
    j = request.json
    key = j['key']
    seconds = j['seconds']
    d[key][1] = time.time() + float(seconds)
    return ''