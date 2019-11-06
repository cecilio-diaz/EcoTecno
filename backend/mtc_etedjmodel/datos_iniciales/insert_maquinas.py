import pandas as pd
import os
from   conexiones_bases_datos import get_data_base
import psycopg2


def insert_maquinas(config):
    data = pd.read_csv("Mtconnect angentes multiples FOMIX DAIMLER SMI-ETE - maquinas.csv")
    
    for i in range(0,len(data)-1,1):
        n = i+1
    
        D         = data.values[n] 
        idScanner = '00:00:00:00:00:00:00'+str(n)

        try:
            QUERY = ("""INSERT INTO public."opcionesGenerales_marcamaquina"("MarcaMaquina") VALUES ('"""+str(D[4])+"""');""")
            conn                   = psycopg2.connect(config)
            cursor = conn.cursor()
            cursor.execute(QUERY)
            conn.commit()
        except:
            print('VALOR_EXISTENTE:',D[4])

        try:
            QUERY  = ("""INSERT INTO public."opcionesGenerales_modelosmaquinas"(
            	          "ModelosMaquinas", "MarcaMaquina_id")
            	           VALUES ('"""+str(D[5])+"""', (SELECT id FROM public."opcionesGenerales_marcamaquina" WHERE "MarcaMaquina"='"""+str(D[4])+"""'));""")
            conn   = psycopg2.connect(config)
            cursor = conn.cursor()
            cursor.execute(QUERY)
            conn.commit()
        except:
            print('VALOR_EXISTENTE:',D[5])
        A = 1
        if A == 1:
    
            ControllerMode       =  D[6]
            ControllerWarning    =  D[7]
            Execution            =  D[8] 
            PartCount            =  D[9]
            PathProgram          =  D[10]
            PathToolNumber       =  D[11]
            cargas_y_movim       =  D[12]     
            valor_unico_programa =  D[13]
   
            QUERY = ("""INSERT INTO public."DatosEmpresa_maquina"(
                maquina,
                "urlMtConnect",
                "tiempoPeticion",
                "idScanner",
                "nodoProcesamiento",
                "hiloProcesamiento",
                empresa_id,
                linea_id, 
                planta_id,
                "ModelosMaquinas_id",
                "MarcaMaquina_id", 
                "NivelDeHabilidadReq",
                "ControllerMode",
                "ControllerWarning", 
                "Execution",
                 "PartCount", 
                "PathProgram",
                "PathToolNumber",
                cargas_y_movim,
                valor_unico_programa)
                VALUES ('"""+str(D[1])+"""',
                        '"""+str(D[3])+"""', 
                        1,
                    '"""+str(idScanner)+"""', 1, 1,
                    (SELECT id FROM public."DatosEmpresa_empresa" WHERE empresa = 'EMPRESA_DEMO'),
                    (SELECT id FROM public."DatosEmpresa_linea" WHERE linea     = 'LINEA_DEMO'),
                    (SELECT id FROM public."DatosEmpresa_planta" WHERE planta   = 'PLANTA_DEMO'),
                    (SELECT id FROM public."opcionesGenerales_modelosmaquinas" WHERE "ModelosMaquinas" = '"""+str(D[5])+"""' limit 1),
                    (SELECT id  FROM public."opcionesGenerales_marcamaquina" WHERE "MarcaMaquina" = '"""+str(D[4])+"""'),
                    3, 
                    '"""+str(ControllerMode)+"""', 
                    '"""+str(ControllerWarning)+"""', 
                    '"""+str(Execution)+"""',
                    '"""+str(PartCount)+"""',
                    '"""+str(PathProgram)+"""',
                    '"""+str(PathToolNumber)+"""',
                    '"""+str(cargas_y_movim)+"""',
                    '"""+str(valor_unico_programa)+"""');""")    
            print(QUERY)
            conn   = psycopg2.connect(config)
            cursor = conn.cursor()
            cursor.execute(QUERY)
            conn.commit()
            conn.close()
            
#        except:
#            print('YA LA MAQUINA  ')

#IP,PUERTO,DB,USER,PASSWORD = get_data_base()
#all_data               = False
#server_postgres        =[IP,PUERTO,DB,USER,PASSWORD] # Conexion Postgres
#config                 = "host= "+ server_postgres[0] + " port="+ server_postgres[1]+  " dbname="+server_postgres[2]+ " user="+server_postgres[3]+ " password="+server_postgres[4]
#conn                   = psycopg2.connect(config)
#insert_maquinas(config)
#
