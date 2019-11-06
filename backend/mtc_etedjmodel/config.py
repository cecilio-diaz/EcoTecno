# THIS FILE CAN TO DO THE CONFIGURATION IP, PASSWORD OF THE SERVICES.
# AUTOR: CECILIO CANNAVACCIUOLO DIAZ
# DATE: 07-20-2019
# DESCRIPTION: CONFIGURTION OF THE DATA FOR START THE SERVICES.

#    LIBRARY
import os
from   datetime import datetime
import socket
import sys
from   os import listdir
import argparse
# // LIBRARY

def config(POSTGRES_KEY,POSTGRES_IP,POSTGRES_PORT,POSTGRES_USER,POSTGRES_PASSWORD,POSTGRES_DB):
    SECRET_KEY = """ '""" +str(POSTGRES_KEY) + """' """
    DB_URL     = ' "postgres://'+str(POSTGRES_USER)+':'+POSTGRES_PASSWORD+'@'+str(POSTGRES_IP)+':'+str(POSTGRES_PORT)+'/'+str(POSTGRES_DB) +'"'

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

POSTGRES_DB       = sys.argv[1]
POSTGRES_PASSWORD = sys.argv[2]
POSTGRES_USER     = sys.argv[3]
POSTGRES_PORT     = sys.argv[4]
POSTGRES_IP       = sys.argv[5]
POSTGRES_KEY      = sys.argv[6]

(POSTGRES_KEY,POSTGRES_IP,POSTGRES_PORT,POSTGRES_USER,POSTGRES_PASSWORD,POSTGRES_DB)

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
