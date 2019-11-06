
import os

def get_data_base(segmento_ruta):
    
    ruta      = os.getcwd()
    cd_actual = ruta
    id_ruta   = ruta.find(segmento_ruta) 
    
    
    ruta      = ruta[0:id_ruta]
   
    
    os.chdir(ruta) 
    # Leer los datos del archivo de configuracion. 

    f = open ('db_config.txt','r')
    datos = f.read()
    #print(mensaje)
    f.close()
    a = -1
    b = 0
    DATOS_1 = []
    DATOS_2 = []
    for i in datos:
        a = a+1
        if i =='!':
            
            if b == 0:
                DATOS_1.append(a)
                b = 1       
            else:
                DATOS_2.append(a)
                b = 0
    DATOS_2.append(a)

    IP         = datos[DATOS_1[0]+1:DATOS_2[0]-0]
    PUERTO     = datos[DATOS_2[0]+1:DATOS_1[1]-0]    
    DB         = datos[DATOS_1[1]+1:DATOS_2[1]-0]
    USER       = datos[DATOS_2[1]+1:DATOS_1[2]-0]
    PASSWORD   = datos[DATOS_1[2]+1:DATOS_2[2]+0]
    
    
    os.chdir(cd_actual)
    return IP,PUERTO,DB,USER,PASSWORD