import requests
import time
import json

def encender(ip, puerto):
    
    url = 'http://172.20.208.'+ip
    datos1 = {"code": "request", "cid": 4, "adr": "/iolinkmaster/port["+puerto+"]/iolinkdevice/pdout/setdata", "data": {"newvalue": "01"}}
    respuesta = requests.post(url, json = datos1)
    Rjson1 = respuesta.json()
    print ("Prendido")


    


while(True):
    mensaje = input("")

    if mensaje == "fresa_e":
        encender('75','1')
        
        
    elif mensaje == "fresa_r":
        encender('75','4')
       
        
    elif mensaje == "torno_e":
        encender('76','7')
        
        
    elif mensaje == "torno_r":
        encender('76','8')
        
        
    elif mensaje == "principal_e":
        encender('77','3')
        
        
    elif mensaje == "principal_r":
        encender('77','4')
        
    elif mensaje == "salir":
        break
    
    