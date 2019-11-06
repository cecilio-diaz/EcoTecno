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


def venditori(number_venditori, latitudine_quadrato, longitudine_quadrato):
    p = {}
    for i in range(number_venditori):
        a = random.uniform(latitudine_quadrato[0], latitudine_quadrato[1]) #latitudine
        b = random.uniform(longitudine_quadrato[0], longitudine_quadrato [1]) #longitudine
        rating = random.uniform(3,5)
        verified = random.choice([True, False])
        Nome = fake.name()
        numero_prodotti = random.randint(1,4)
        identificativo = [0,1,2,3,4]
        prodotti = []
        for k in range(numero_prodotti):
            prodotti= random.sample(identificativo, k = numero_prodotti)
        immagine = random.randint(1, 60)
        ima = 'https://i.pravatar.cc/150?img={}'.format(immagine)
        p[i]= {'name': Nome, 'Rating' : rating, 'verified': verified, 'lat':a, 'lon':b,'prodotti': prodotti,'city':'Milano', 'image' :ima}
    return p


# In[504]:


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
    p = {'id':identificativo, 'name': nome_prodotto, 'foto prodotto' : foto, 'descrizione': descrizione}
    return p




def sensore_umidity(humidity):
    s = random.randint(-2,2)
    humidity = np.mean(humidity)
    lista = round(humidity+s)
    p = {"dataSource": 'sensore umidità', 'status': True, "IoTdevice": "arduino", 'value':lista, 'unit': "%"}

{
    "id": 1,
    "seller": 1,
    "date_create": "2019-11-06T18:45:19.942584+01:00",
    "country": "Mexico",
    "city": "San Nicolas",
    "dataSource": "2",
    "status": false,
    "IoTdevice": "4",
    "SensorType": "tempertura",
    "value": 32,
    "unit": "entre calles Gabilondo Soler y Felipe Villanuva"
}

    return p

def sensore_temperatura(temperatura_terreno, lat, lon):
    s = random.randint(-2,2)
    temperatura_terreno = np.mean(temperatura_terreno)
    lista = temperatura_terreno+s
    p = {"dataSource": 'sensore temepratura', 'status': True, "IoTdevice": "arduino", 'value':lista, "unit": "C"}
    return p

def sensore_inquinante():
    d = random.uniform(-8, 30)
    pm_10 = [14,13.3, 12.8, 11.1, 10.4, 12.9, 11.3, 10.1, 15.8, 19.2, 21.8, 21.1, 24, 30.3, 24.1, 26.7]
    pm_10 = np.mean(pm_10)
    lista=round(((pm_10+d)/61.2)*100,2)
    if lista > 60:
        toxicity=True
    else:
        toxicity = False

    p = {"dataSource": 'sensore inquinamento', 'status': True, "IoTdevice": "arduino", 'value':lista, 'Tossicità' : toxicity, 'unit': "%"}
    return p
