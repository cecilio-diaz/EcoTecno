import pandas as pd
import os
from   conexiones_bases_datos import get_data_base
import psycopg2

def insert_variables_de_control_por_default(config):
    data = pd.read_csv("FOMIX DAIMLER SMI-ETE Variables_de_control - Sheet1.csv")
    for nn in range(0,len(data),1):
        n         = nn
        D         = data.values[n]

        Execution = D[3]
        Modo      = D[2]
        Alarma    = D[4]
        QUERY     = ("""SELECT id,"MarcaMaquina" FROM public."opcionesGenerales_marcamaquina";""")
        conn      = psycopg2.connect(config)
        cursor    = conn.cursor()
        cursor.execute(QUERY)
        conn.commit()
        MARCA_MAQUINA = []
        for i in cursor:
            ID           = i[0]
            MarcaMaquina = i[1]
            if MarcaMaquina != 'Marca_Prueba':
                MarcaMaquina_id = ID
                
                QUERY = ("""SELECT id FROM public."opcionesGenerales_modelosmaquinas" WHERE "MarcaMaquina_id" = """+str(ID)+""" ORDER BY ID DESC LIMIT 1;""")
                conn                   = psycopg2.connect(config)
                cursor = conn.cursor()
                cursor.execute(QUERY)
                conn.commit()
                for i3 in cursor:
                    ModelosMaquinas_id = i3[0]
  
                    QUERY  = ("""SELECT id,indicacion FROM public.gestion_causastm WHERE "CausasTm" = '"""+str(D[6])+"""'""")
                    cursor = conn.cursor()
                    cursor.execute(QUERY)
                    conn.commit()
                    for i4 in cursor:
                        CausasTM_id = i4[0]
                        print CausasTM_id
                        indicacion  = i4[1]
                        QUERY = ("""INSERT INTO public."opcionesGenerales_variablesdelcontrol"(
                                "MarcaMaquina_id", "ModelosMaquinas_id",
                                "Execution", "Modo", "Alarma",
                                "CausasTM_id", "Prioridad_id", indicacion, "CorteViruta")
                                VALUES ('"""+str(MarcaMaquina_id)+"""', '"""+str(ModelosMaquinas_id)+"""',
                                '"""+str(Execution)+"""', '"""+str(Modo)+"""', '"""+str(Alarma)+"""',
                                """+str(CausasTM_id)+""", """+str(int(D[7]))+""",'"""+str(indicacion)+"""',"""+str(D[5])+""");""")
                        cursor = conn.cursor()
                        cursor.execute(QUERY)
                        conn.commit()

#from insert_causasTM_multi_agentes import  insert_variables_de_control_por_default
IP,PUERTO,DB,USER,PASSWORD = get_data_base()
all_data                   = False
server_postgres            =[IP,PUERTO,DB,USER,PASSWORD] # Conexion Postgres
config                     = "host= "+ server_postgres[0] + " port="+ server_postgres[1]+  " dbname="+server_postgres[2]+ " user="+server_postgres[3]+ " password="+server_postgres[4]
conn                       = psycopg2.connect(config)
insert_variables_de_control_por_default(config)
