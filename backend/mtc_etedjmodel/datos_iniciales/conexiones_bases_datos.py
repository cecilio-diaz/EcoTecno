# Obtener el ID scanner empleando los datos
from datetime import datetime
import psycopg2
import os
import os.path as path

def get_data_base():
    
    # Leer los datos del archivo de configuracion. 

    f = open ('db_config.txt','r')
    datos = f.read()
#    print datos
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
    PASSWORD   = datos[DATOS_1[2]+1:DATOS_2[2]+1]
    
    
   
    return IP,PUERTO,DB,USER,PASSWORD

#IP,PUERTO,DB,USER,PASSWORD = get_data_base()
#print IP,PUERTO,DB,USER,PASSWORD

def get_buffer_scanner_data(conn,maquina,causaTM):
    
    mac_adress   = ''
    causasTM_id  = 0
    codigo       = ''
    Prioridad_id = 0
    Prioridad    = 3
    indicacion  = 'NO DEFINIDA'
    
    QUERY = ("""SELECT "idScanner"
                FROM public."DatosEmpresa_maquina"
                WHERE (maquina = '"""+str(maquina)+"""')""")
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit() 

    E1 = True  # idScanner
    E2 = True  # id
    E3 = True  # codigoID
    E4 = True  # Prioridad_id
    E5 = True  # Prioridad

    for i in cursor:
        E1 = False
        mac_adress = i[0]
    
        # Obtener los datos de CausaTM.
        QUERY = ("""SELECT id
                    FROM public.gestion_causastm
                    WHERE "CausasTm" = '"""+str(causaTM)+"""'""") 
        
       
        cursor = conn.cursor()
        cursor.execute(QUERY)
        conn.commit()
    
        for i2 in cursor:
            E2 = False
        
            causasTM_id = i2[0]
    
            QUERY = ("""SELECT  "codigoID"
                         FROM public.gestion_scanner
                         WHERE "CausasTm_id" = """+str(causasTM_id)+""" """)
        
            cursor = conn.cursor()
            cursor.execute(QUERY)
            conn.commit()    
        
            
            for i3 in cursor:
                E3 = False
            
                codigo = i3[0]
                
                QUERY = ("""SELECT "Prioridad_id",indicacion
                            FROM public."opcionesGenerales_variablesdelcontrol"
                            WHERE ("CausasTM_id" = """+str(causasTM_id)+""") limit 1""")

                cursor = conn.cursor()
                cursor.execute(QUERY)
                conn.commit()  
            
                for i4 in cursor:
                    E4 = False
                    Prioridad_id = i4[0]
                    indicacion   = i4[1]
                    
                    QUERY = ("""SELECT "Prioridad"
                                FROM public."opcionesGenerales_prioridad"
                                WHERE id = """+str(Prioridad_id)+"""""")
                
                    cursor = conn.cursor()
                    cursor.execute(QUERY)
                    conn.commit()     

                    for i5 in cursor:
                        E5 = False
                        Prioridad  = i5[0]
                        
            
                        
    ERROR = ''                 
    if E1 == True:
        ERROR =('E1 NO SE ENCUENTRA EN LA BD idScanner')
    elif E2 == True:
        ERROR = ('E2 NO SE EN LA BD del ID')
    elif E3 == True:
        ERROR = ('E3 NO SE EN LA BD el codigoID')
#    elif E4 == True:
#        ERROR = ('E4 NO SE EN LA BD el valor de  Prioridad_id')
#    elif E5 == True:
#        ERROR = ('E5 NO SE EN LA BD el valor de  Prioridad')
        
        
#    f = open ('antes2.txt','w')
#    f.write(mac_adress)
#    f.write(causasTM_id)
#    f.write(codigo)
#    f.write(Prioridad_id)
#    f.write(Prioridad,indicacion)
##    f.write(indicacion)
##    f.write(ERROR)
#    f.close()

                           
    return mac_adress,causasTM_id,codigo,Prioridad_id,Prioridad,indicacion,ERROR