#Universidad Simon Bolivar
#Redes definidas por Software
#Vladimir Alfaro 15-10023
#Practica 2

import os 
from pprint import pprint
import requests 
import json
import yaml
import xmltodict
import csv

#1. Le solicitaron una función para listar todas las organizaciones a las que tiene usted acceso con el API Key.

url = "https://api.meraki.com/api/v1/organizations"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

response = requests.get(url, headers = headers, data = payload)

organizations = response.text.encode('utf8')
organizations_json = response.json()
pprint(organizations_json)

#2.- Al hacer la entrega, le solicitan crear un repositorio en el servicio de su preferencia 
#(github, gitlab, bitbucket, etc.) para almacenar todo su código y compartirlo con la compañía.
#Su primer commit debe contener el código y un archivo README con instrucciones básicas para utilizarlo.

#5 Validacion de cada solicitud

status = response.raise_for_status()
print('Validacion: ', status)

#3 Inventario de los dispositivos en la red 

url1 = "https://api.meraki.com/api/v1/organizations/681155/devices"

payload1 = None

headers1 = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

response = requests.get(url1, headers = headers1, data = payload1)
#pprint(response.json())


response_list = response.json()
wireless_list = []
appliance_list = []


for device in response_list:
    if device['productType'] == 'wireless':
        wireless_list.append(device)
    if device['productType'] == 'appliance':
        appliance_list.append(device)

#pprint(wireless_list)
#pprint(appliance_list)

features = ['Tipo', 'Modelo', 'Nombre', 'MAC', 'IP LAN', 'Serial', 'Estatus']

with open("dispositivos.csv", 'w') as f:
    writer_f = csv.writer(f)
    writer_f.writerow(features)
    f.close()

for device in wireless_list:
    device_feature = []
    device_feature.append(device['productType'])
    device_feature.append(device['model'])
    device_feature.append(device['name'])
    device_feature.append(device['mac'])
    device_feature.append(device['lanIp'])
    device_feature.append(device['serial'])
    device_feature.append(device['configurationUpdatedAt'])
    with open("dispositivos.csv", 'a', newline = '') as f:
        writer_f = csv.writer(f)
        writer_f.writerow(device_feature)
    f.close()

