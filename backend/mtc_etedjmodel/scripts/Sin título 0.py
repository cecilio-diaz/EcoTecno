import requests
import json

URL      = 'https://api.openaq.org/v1/measurements?limit=10'
data     = requests.get(URL)
data     = data.json()


meta      = data['meta']
license2  = meta['license']
website   = meta['website']
page      = meta['page']
limit     = meta['limit']




results   = data['results']

for i in results:
    resutls = i
    
    print(i)

    location  = resutls['location']
    parameter = resutls['parameter']

    date       = i['date']
    date_utc   = date['utc']
    date_local = date['local']

    value       = i['value']
                        
    coordinates = i['coordinates']

    latitude    = coordinates['latitude']
    longitude   = coordinates['longitude']
    country     = i['country']
    city        = i['city']


    print(city,latitude,longitude,value)

