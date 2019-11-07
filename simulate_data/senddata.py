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
fake = Faker('it_IT')
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

def sensore_inquinante(ID_user):
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

def venditori(number_venditori, latitudine_quadrato, longitudine_quadrato):
    profilo = {}
    na = []
    for i in range(number_venditori):
        a = random.uniform(latitudine_quadrato[0], latitudine_quadrato[1]) #latitudine
        b = random.uniform(longitudine_quadrato[0], longitudine_quadrato [1]) #longitudine
        rating = random.uniform(3,5)
        verified = random.choice([True, False])
        Nome = fake.name()
        numero_prodotti = random.randint(1,4)
        identificativo = [1,2,3,4,5]
        prodotti = []
        for k in range(numero_prodotti):
            prodotti= random.sample(identificativo, k = numero_prodotti)
        immagine = random.randint(1, 60)
        
        ima = 'https://i.pravatar.cc/150?img={}'.format(immagine)
        profilo[i]= {'profile': Nome, 'Rating' : rating, 'verified': verified, 'latitude':a, 'longitude':b,'image' :ima}
    return profilo

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
            print('Inserted fake humidity')
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
            print('Inserted fake temp')
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
        if code == 200 or code == 201:
            print('Inserted fake toxicity')
        elif code == 400:
            print('ERROR SOLICITUD INCORRECTA')
        elif code == 500:
            print('ERROR INTERNO DEL SERVIDOR')

def prodotto(nome_prodotto):
    if nome_prodotto == 'pomodoro':
        foto = 'https://blog.giallozafferano.it/robyfoodandlove/wp-content/uploads/2018/03/1-960x960.jpg'
        descrizione = 'rosso e invitante'
        identificativo = 0
    elif nome_prodotto == 'zucchine':
        foto = 'https://www.gustissimo.it/articoli/ricette/antipasti-verdure/carpaccio-di-zucchine.jpg'
        descrizione = 'buone e salutari'
        identificativo = 1
    elif nome_prodotto == 'carote':
        descrizione = 'le preferite da Bugs Bunny'
        identificativo = 2
        foto = 'https://static.tantasalute.it/r/845X0/www.tantasalute.it/img/carote_proprieta_-nutrizionali_benefiche_calorie.jpg'
    elif nome_prodotto == 'cavolfiore':
        foto = 'https://file.cure-naturali.it/site/image/content/22030.jpg?format=jpg'
        descrizione = 'ricercato e molto sfizioso'
        identificativo = 3
    else:
        nome_prodotto = 'lattuga'
        foto = 'https://www.panierebio.com/418-large_default/lattuga-varia-biologica.jpg'
        descrizione = 'buona tutto l\'anno'
        identificativo = 4
    p = {'id':identificativo, 'product': nome_prodotto, 'image' : foto, 'description': descrizione}
    return p

def venditori_prodotti(ID_user,ID_prodotti):
    numero_prodotti = random.randint(1,5)
    prodotti = []
    for k in range(numero_prodotti):
        prodotti= random.sample(ID_prodotti, k = numero_prodotti)
    prodotti_venduti = {'sellers':ID_user, 'prodotti': prodotti}
    return prodotti_venduti

def assegnazione(url):
    sellers_url = str(url)+'/api/v1/sellers/'
    prodotti_url = str(url) +'/api/v1/product/'
    api_post_datos_dato = str(url)+'/api/v1/seller_product/'
    data_api= requests.get(sellers_url)
    data_api_2 = requests.get(prodotti_url)
    data= data_api.json()
    data= data['results']
    data_2= data_api_2.json()
    data_2= data_2['results']
    ID_prodotti = []
    for j in data_2:
        ID_prodotti.append(j['id'])
    for i in data:
        ID_user = i['id']
        print(ID_user)
        data_s = venditori_prodotti(ID_user, ID_prodotti)
        solicitud = requests.post(api_post_datos_dato, data = data_s)
        code= solicitud.status_code
        print(data_s)

url      = sys.argv[1]

lista_prodotti = ['pomodoro', 'zucchine', 'cavolfiore', 'carote', 'lattuga']
for p in lista_prodotti:
    response = requests.post('{}/api/v1/product/'.format(url), data = prodotto(p))
    print(response)

print('Inserted prodotti')

latitudine = [45.337227, 45.529266]
longitudine = [9.089094, 9.394036]
data = venditori(5,latitudine,longitudine)
for i in range(5):
    response = requests.post('{}/api/v1/sellers/'.format(url), data = data[i])
    print(response)
print('Inserted venditori')

assegnazione(url)
print('Assigned products to sellers')

while True:
    try:
        insert_data_sensor(url)
        print('Inserted sensor data')
    except:
        print('Error during inserting sensor data')
    time.sleep(60)
