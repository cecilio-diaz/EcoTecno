# THIS FILE CAN TO DO THE CONFIGURATION IP, PASSWORD OF THE SERVICES.
# AUTOR: CECILIO CANNAVACCIUOLO DIAZ
# DATE: 07-20-2019
# DESCRIPTION: CONFIGURTION OF THE DATA FOR START THE SERVICES.

#    LIBRARY
import os
from datetime import datetime
import socket
import sys
from os import listdir


import argparse
# // LIBRARY

def config(IP,PUERTO,USER,PASSWORD,DB):

    SECRET_KEY = """ '0k^k))ac-zp$6)6f+bljru0e-!fx175hanut(93_5l*t2(@3@1' """
    DB_URL     = ' "postgres://'+str(USER)+':'+PASSWORD+'@'+str(IP)+':'+str(PUERTO)+'/'+str(DB) +'"'

    print('--------------*---------------*--------------*')
    print(DB_URL)
    print('--------------*---------------*--------------*')


    os.chdir('.')
    file = open('.env','w')
    file.write('SECRET_KEY='+SECRET_KEY+' \n')
    file.write('DB_URL='     +DB_URL+' \n')
    file.close()

    try:
        os.chdir('/django_app')
        file = open('.env','w')
        file.write('SECRET_KEY='+SECRET_KEY+' \n')
        file.write('DB_URL='     +DB_URL+' \n')
        file.close()
    except:
        print('Ruta del contenedor no disponible para config')

IP       = sys.argv[1]
PUERTO   = sys.argv[2]
USER     = sys.argv[3]
PASSWORD = sys.argv[4]
DB       = sys.argv[5]

print(IP,PUERTO,USER,PASSWORD,DB)
config(IP,PUERTO,USER,PASSWORD,DB)

print('------------------------------------------------')
print('------------------------------------------------')
print('------------------------------------------------')
print()
print('CONFIGURACION DE ARCHIVO....')
print('IP       :' ,IP)
print('PUERTO   :',PUERTO)
print('USER     :',USER)
print('DB       :',DB)
print('PASSWORD :',PASSWORD)
print()
print()
print(os.getcwd())
print()
print('CONTENIDO DEL DIRECTORIO:')
print()
print(listdir(os.getcwd()))
print()
print('------------------------------------------------')
print(listdir('.'))
print('------------------------------------------------')
archivo = open(".env", "r")
for linea in archivo.readlines():
    print(linea)
archivo.close()
print('------------------------------------------------')

# python config.py "10.0.75.1" "35432" "postgres" "galileo.1564" "smx_mt_connect_app"
