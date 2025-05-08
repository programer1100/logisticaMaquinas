import requests

mensaje = input("")
if(mensaje=="torno"):
    ip='76'
    amarilla="2"
    verde="3"
    roja="1"
elif(mensaje=="fresa"):
    ip='75'
    amarilla="6"
    verde="5"
    roja="7"


url = 'http://172.20.208.'+ip
datos1 = {"code": "request", "cid": 4, "adr": "/iolinkmaster/port["+verde+"]/iolinkdevice/pdout/setdata", "data": {"newvalue": "00"}}
respuesta2 = requests.post(url, json = datos1)
Rjson1 = respuesta2.json()

url = 'http://172.20.208.'+ip
datos1 = {"code": "request", "cid": 4, "adr": "/iolinkmaster/port["+roja+"]/iolinkdevice/pdout/setdata", "data": {"newvalue": "00"}}
respuesta2 = requests.post(url, json = datos1)
Rjson1 = respuesta2.json()

url = 'http://172.20.208.'+ip
datos1 = {"code": "request", "cid": 4, "adr": "/iolinkmaster/port["+amarilla+"]/iolinkdevice/pdout/setdata", "data": {"newvalue": "01"}}
respuesta = requests.post(url, json = datos1)
Rjson1 = respuesta.json()