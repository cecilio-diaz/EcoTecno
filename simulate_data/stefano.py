
import requests
import pandas as pd
import lxml.html as lh
import numpy as np
import json
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import random
from faker import Faker
fake = Faker('it_IT')


# In[2]:


website_url = requests.get("https://weather.com/it-IT/tempo/orario/l/6d9db4b0c02eca06aed6e417fc47f979b535ef29645c444ee0001e9815a7af65")
doc = lh.fromstring(website_url.content)


# In[3]:


tr_elements = []
for i in range(1,100):
    try:
        tr_elements.append(doc.xpath('//*[@id="twc-scrollabe"]/table/tbody/tr[{}]/td[4]/span'.format(i)))
    except:
        pass
    col=[]
for i in range(len(tr_elements)):
    try:
        name=tr_elements[i][0].text_content()
        col.append((name))
    except:
        pass


# In[4]:


tr_elements_2 = []
for i in range(1,100):
    try:
        tr_elements_2.append(doc.xpath('//*[@id="twc-scrollabe"]/table/tbody/tr[{}]/td[7]/span/span'.format(i)))
    except:
        pass
col_2=[]
for i in range(len(tr_elements_2)):
    try:
        name=tr_elements_2[i][0].text_content()
        col_2.append((name))
    except:
        pass


# In[5]:


tr_elements_3 = []
for i in range(1,100):
    try:
        tr_elements_3.append(doc.xpath('//*[@id="twc-scrollabe"]/table/tbody/tr[{}]/td[3]/span'.format(i)))
    except:
        pass
col_3=[]
for i in range(len(tr_elements_3)):
    try:
        name=tr_elements_3[i][0].text_content()
        col_3.append((name))
    except:
        pass


# In[6]:


tr_elements_4 = []
for i in range(1,100):
    try:
        tr_elements_4.append(doc.xpath('//*[@id="twc-scrollabe"]/table/tbody/tr[{}]/td[2]/div/div[1]/span'.format(i)))
    except:
        pass
col_4=[]
for i in range(len(tr_elements_4)):
    try:
        name=tr_elements_4[i][0].text_content()
        col_4.append((name))
    except:
        pass


# In[7]:


tr_elements_3 = []
for i in range(1,100):
    try:
        tr_elements_3.append(doc.xpath('//*[@id="twc-scrollabe"]/table/tbody/tr[{}]/td[3]/span'.format(i)))
    except:
        pass
col_3=[]
for i in range(len(tr_elements_3)):
    try:
        name=tr_elements_3[i][0].text_content()
        col_3.append((name))
    except:
        pass


# In[209]:


col_5 = pd.DataFrame(pd.concat([pd.Series(col_4),pd.Series(col_3),pd.Series(col),pd.Series(col_2)], axis = 1)).rename(columns={0: 'Orario', 1:'Descrizione', 2:'Temperatura', 3:'Umidità'})
col_5['Temperatura terreno'] = 0
col_5['Umidità terreno'] = 0
for i in range(len(col_5)):
    if len(col_5['Temperatura'][i]) == 2:
        col_5['Temperatura terreno'][i] = pd.to_numeric(col_5['Temperatura'][i][:1]) + random.randint(2,4)
        col_5['Temperatura'][i] = pd.to_numeric(col_5['Temperatura'][i][:1])
    else:
        col_5['Temperatura terreno'][i] = pd.to_numeric(col_5['Temperatura'][i][:2]) + random.randint(2,4)
        col_5['Temperatura'][i] = pd.to_numeric(col_5['Temperatura'][i][:2])
    col_5['Umidità terreno'][i] = pd.to_numeric(col_5['Umidità'][i][:2]) + 0.03*pd.to_numeric(col_5['Umidità'][i][:2])
    col_5['Umidità'][i] = pd.to_numeric(col_5['Umidità'][i][:2])


# In[210]:


col_5


# # Venditori

# In[220]:


latitudine = [45.337227, 45.529266]
longitudine = [9.089094, 9.394036]


# In[506]:


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
lista_prodotti = ['pomodoro', 'zucchine', 'cavolfiore', 'carote', 'lattuga']
diz = []
for i in lista_prodotti:
    diz.append(prodotto(i))


# In[527]:


def sensore_umidity(humidity):
    s = random.randint(-2,2)
    humidity = np.mean(humidity)
    lista = round(humidity+s)
    p = {"dataSource": 'sensore umidità', 'status': True, "IoTdevice": "arduino", 'value':lista, 'unit': "%"}
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


# In[530]:


a = sensore_umidity(col_5['Umidità terreno'])


# In[533]:


b = venditori(6, latitudine,longitudine)
b


# In[535]:


code = requests.post('http://90.147.184.214/api/v1/sellers/',data = b)
print(code.__dict__)
