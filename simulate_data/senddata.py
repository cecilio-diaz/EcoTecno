import requests
import json
import random
import requests
import pandas as pd
import lxml.html as lh
import numpy as np
import json
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")
import random
from faker import Faker
import time
import sys


def sensore_umidity(humidity, ID_user):
    s = random.randint(-2,2)
    humidity = np.mean(humidity)
    lista = round(humidity+s)
    p= {"dataSource": 'sensore umidità', 'status': True, "IoTdevice": "arduino", 'value':lista, 'unit': "%", 'seller':ID_user}
    return p

def sensore_temperatura(temperatura_terreno,ID_user):
    s = random.randint(-2,2)
    temperatura_terreno = np.mean(temperatura_terreno)
    lista = []
    lista = round(temperatura_terreno+s)
    p = {"dataSource": 'sensore temepratura', 'status': True, "IoTdevice": "arduino", 'value':lista, "unit": "C", 'seller' : ID_user}
    return p

def sensore_inquinante(Nome):
    d = random.uniform(-8, 30)
    pm_10 = [14,13.3, 12.8, 11.1, 10.4, 12.9, 11.3, 10.1, 15.8, 19.2, 21.8, 21.1, 24, 30.3, 24.1, 26.7]
    pm_10 = np.mean(pm_10)
    lista=round(((pm_10+d)/61.2)*100)
    if lista > 60:
        toxicity=True
    else:
        toxicity = False

    p= {"dataSource": 'sensore inquinamento', 'status': True, "IoTdevice": "arduino", 'value':lista, 'Tossicità' : toxicity, 'unit': "%",
                   'seller' : ID_user}
    return p




def insert_data_sensor(url):

    sellers_url         = str(url)+'/api/v1/sellers/'
    api_post_datos_dato = str(url)+'/api/v1/services/'


    temperatura = [13, 13, 13, 15, 14, 14, 14, 15, 13, 13, 13, 13, 11, 10, 11, 9]
    umidity     = [91, 91, 90, 86, 86, 81, 83, 86, 92, 92, 94, 95, 96, 98, 97, 97]

    data_api       = requests.get(sellers_url)
    data           = data_api.json()
    data           = data['results']

    for i in data:
        ID_user = i['id']
        print(ID_user)

        ################ sensore_umidity
        data_s = sensore_umidity(umidity, ID_user)
        print(data_s)
        solicitud = requests.post(api_post_datos_dato, data = data_s)
        code      = solicitud.status_code
        print(code)
        if code == 200 or code == 201 :
            A = 1
            # print('API: DATOS_INSERTADOS')
        elif code == 400:
            print('ERROR SOLICITUD INCORRECTA')
        elif code == 500:
            print('ERROR INTERNO DEL SERVIDOR')

        ################ sensore_umidity
        ################ temperatura
        data_s = sensore_temperatura(temperatura, ID_user)
        print(data_s)
        solicitud = requests.post(api_post_datos_dato, data = data_s)
        code      = solicitud.status_code
        print(code)
        if code == 200 or code == 201 :
            A = 1
            # print('API: DATOS_INSERTADOS')
        elif code == 400:
            print('ERROR SOLICITUD INCORRECTA')
        elif code == 500:
            print('ERROR INTERNO DEL SERVIDOR')

        ################ inquinante
        data_s = sensore_inquinante( ID_user)
        print(data_s)
        solicitud = requests.post(api_post_datos_dato, data = data_s)
        code      = solicitud.status_code
        print(code)
        if code == 200 or code == 201 :
            A = 1
            # print('API: DATOS_INSERTADOS')
        elif code == 400:
            print('ERROR SOLICITUD INCORRECTA')
        elif code == 500:
            print('ERROR INTERNO DEL SERVIDOR')


# url = 'http://90.147.184.214'
ruta     = sys.argv[0]
url      = sys.argv[1]

while True:
    try:
        insert_data_sensor(url)
        print('OK: INSERT DATA')
    except:
        print('error')
    time.sleep(60)
