import requests, json

url = 'http://127.0.0.1:5000/'
while True:
    i = input().strip().split()
    if i[0] == 'GET':
        d = {'key': i[1]}
        requests.get(url+i[0], data=json.dumps(d))
    else:
        d = dict()
        d['key'] = i[1]
        if i[0] == 'SET':
            d['value'] = i[2]
        else:
            d['seconds'] = i[2]
        requests.post(url+i[0], data=json.dumps(d))