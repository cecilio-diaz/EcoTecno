import psycopg2
from   datetime    import datetime, time, timedelta
import socket
import pandas as pd
import os
from conexiones_bases_datos import get_data_base
from insert_maquinas import insert_maquinas

from insert_causasTM_multi_agentes import  insert_variables_de_control_por_default


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IP_ROOT = os.path.join(BASE_DIR,'db_config.txt')

ruta_actual = os.getcwd()
try:
    os.chdir('/datos_iniciales_dj01')
except:
    try:
        os.chdir('/datos_iniciales')
    except:
        print('WORK FROM WINDOWS')

#IP_ROOT = IP_ROOT[0:len(IP_ROOT)-len('db_config.txt')]


IP,PUERTO,DB,USER,PASSWORD = get_data_base()

print(IP,PUERTO,DB,USER,PASSWORD)
#os.chdir(ruta_actual)


all_data               = False
server_postgres        =[IP,PUERTO,DB,USER,PASSWORD] # Conexion Postgres
config                 = "host= "+ server_postgres[0] + " port="+ server_postgres[1]+  " dbname="+server_postgres[2]+ " user="+server_postgres[3]+ " password="+server_postgres[4]
conn                   = psycopg2.connect(config)



insert_maquinas(config)


try:
    QUERY = (""" DELETE FROM public."DatosEmpresa_empresa";
                 DELETE FROM public.gestion_causastm;
                 DELETE FROM public.gestion_clasificacionete;
                 DELETE FROM public.gestion_seisperdidas;
                 DELETE FROM public.gestion_areas;
                 DELETE FROM public.gestion_gestionete;
                 DELETE FROM public."opcionesGenerales_modelosmaquinas";
                 DELETE FROM public."opcionesGenerales_prioridad";
                 DELETE FROM public."opcionesGenerales_marcamaquina";
                 DELETE FROM public."opcionesGenerales_tipodetarea";
                 DELETE FROM public."opcionesGenerales_estado";

        """)
    conn                   = psycopg2.connect(config)
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit()
except:
    print('ERROR EN ELIMINAR DATOS')

A = 1
try:
    QUERY = ("""INSERT INTO public."DatosProceso_cirterio_cambio_pieza"(cirterio_cambio_pieza) VALUES ('cambio_de_palet');""")
    conn                   = psycopg2.connect(config)
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit()
except:
    print('ERROR EN LOS DATOS: cambio_de_palet')

#QUERY = ("""INSERT INTO public."DatosProceso_cirterio_cambio_pieza"(cirterio_cambio_pieza) VALUES ('cambio_de_palet-ciclo_en_vacio');""")
#
#cursor = conn.cursor()
#cursor.execute(QUERY)
#conn.commit()

try:
    QUERY = ("""INSERT INTO public."DatosProceso_cirterio_cambio_pieza"(cirterio_cambio_pieza) VALUES ('conteo_por_ciclo_cnc');""")
    conn                   = psycopg2.connect(config)
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit()
except:
    print('ERROR DATO REPETIDO: conteo_por_ciclo_cnc')

#########################################################
# Insertar las areas que seran insertadas por defaul
#########################################################

AREA = ['operaciones',
        'mantenimiento',
        'manufactura',
        'calidad',
        'herramientas',
        'materiales',
        'NA']



for i in AREA:

    QUERY = ("""INSERT INTO public.gestion_areas(
	            areas)
	            VALUES ('"""+str(i)+"""');""")

    try:
        conn                   = psycopg2.connect(config)
        cursor = conn.cursor()
        cursor.execute(QUERY)
        conn.commit()
    except:
        print('DATO EXISTENTE: ',str(i))


#####################################################################
A = 1
try:

    QUERY = ("""INSERT INTO public."DatosEmpresa_empresa"(empresa)
                VALUES ('EMPRESA_DEMO');""")
    conn                   = psycopg2.connect(config)
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit()
except:
    print('DATO REPETIDO')

A = 1
try:
    QUERY = ("""INSERT INTO public."DatosEmpresa_planta"(planta, empresa_id)
                VALUES ('PLANTA_DEMO', (SELECT id
                FROM public."DatosEmpresa_empresa"
                WHERE (empresa = 'EMPRESA_DEMO')
                LIMIT 1));""")



    conn                   = psycopg2.connect(config)
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit()
except:
    print('DATO REPETIDO: EMPRESA_DEMO')

if A == 1:
    QUERY = ("""INSERT INTO public."DatosEmpresa_linea"(
                linea, empresa_id, planta_id)
                VALUES ('LINEA_DEMO',(SELECT id
                FROM public."DatosEmpresa_empresa"
                WHERE (empresa = 'EMPRESA_DEMO') LIMIT 1), (SELECT id
                FROM public."DatosEmpresa_planta"
                WHERE (planta = 'PLANTA_DEMO') LIMIT 1));""")
    conn                   = psycopg2.connect(config)
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit()

    print('INSERTADO DATOS POR DEFECTO EN: public."DatosEmpresa_linea"')

#except:
#    print('DATO REPETIDO')

try:
    QUERY = ("""INSERT INTO public."opcionesGenerales_modelosmaquinas"(
    	         "ModelosMaquinas", "MarcaMaquina_id")
    	         VALUES ('Modelo_Prueba',(SELECT id
                FROM public."opcionesGenerales_marcamaquina"
                WHERE ("MarcaMaquina" = 'Marca_Prueba')));""")
    conn                   = psycopg2.connect(config)
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit()
    print('INSERTADO DATOS POR DEFECTO EN: public."opcionesGenerales_modelosmaquinas"')
except:
    print('DATO REPETIDO')


try:
    QUERY = ("""INSERT INTO public."DatosEmpresa_maquina"(
                maquina, "urlMtConnect", "tiempoPeticion", "idScanner", "nodoProcesamiento", "hiloProcesamiento", empresa_id, linea_id, planta_id,"MarcaMaquina_id","ModelosMaquinas_id")
                VALUES ('MAQUINA_DEMO', 'http://mtconnect.mazakcorp.com:5609/current',
    		      1, '00:00:00:00:00:00', 1, 1,(SELECT id
                FROM public."DatosEmpresa_empresa"
                WHERE (empresa = 'EMPRESA_DEMO') LIMIT 1),(SELECT id
                FROM public."DatosEmpresa_linea"
                WHERE (linea = 'LINEA_DEMO') LIMIT 1),(SELECT id
                FROM public."DatosEmpresa_planta"
                WHERE (planta = 'PLANTA_DEMO') LIMIT 1),(SELECT id FROM public."opcionesGenerales_marcamaquina" WHERE "MarcaMaquina" = 'Marca_Prueba'),
                (SELECT id FROM public."opcionesGenerales_modelosmaquinas" WHERE ("MarcaMaquina_id" = (SELECT id FROM public."opcionesGenerales_marcamaquina" WHERE "MarcaMaquina" = 'Marca_Prueba') and "ModelosMaquinas" = 'Modelo_Prueba')));""")
    conn                   = psycopg2.connect(config)
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit()

    print('INSERTADO DATOS POR DEFECTO EN: public."DatosEmpresa_maquina"')
except:
    print('DATO REPETIDO')



# CLASIFICACION ETE
#####################################################################
CLASIFICACION_ETE = [
        'disponibilidad',
        'eficiencia',
        'calidad',
        'otros',
        'NA'
        ]


for i in CLASIFICACION_ETE:
    try:
        QUERY = ("""INSERT INTO public.gestion_clasificacionete(
	            "clasificacionEte")
	            VALUES ('"""+str(i)+"""');""")

        conn                   = psycopg2.connect(config)
        cursor = conn.cursor()
        cursor.execute(QUERY)
        conn.commit()
    except:
        print('VALOR REPETIDO')

##################################################################
# CAUSAS TM
##################################################################
try:
    QUERY = ("""INSERT INTO public.gestion_coloralerta("colorAlerta") VALUES ('VERDE');
                INSERT INTO public.gestion_coloralerta("colorAlerta") VALUES ('AMARILLO');
                INSERT INTO public.gestion_coloralerta("colorAlerta") VALUES ('ROJO');
                INSERT INTO public.gestion_coloralerta("colorAlerta") VALUES ('DESACTIVADO');""")
    conn                   = psycopg2.connect(config)
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit()
except:
    print('DATO REPETIDO')

try:
    QUERY = ("""INSERT INTO public.gestion_modoalerta("modoAlerta") VALUES ('CONTINUO');
                INSERT INTO public.gestion_modoalerta("modoAlerta") VALUES ('INTERMITENTE');
                INSERT INTO public.gestion_modoalerta("modoAlerta") VALUES ('NA');""")
    conn                   = psycopg2.connect(config)
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit()
except:
    print('DATO REPETIO')

try:
    QUERY = ("""INSERT INTO public.gestion_sonido(sonido) VALUES ('CONTINUO');
            INSERT INTO public.gestion_sonido(sonido) VALUES ('INTERMITENTE');
            INSERT INTO public.gestion_sonido(sonido) VALUES ('MUTE');
            INSERT INTO public.gestion_sonido(sonido) VALUES ('NA');""")
    conn                   = psycopg2.connect(config)
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit()
except:
    print('DATO REPETIO')


try:
    QUERY = ("""
         INSERT INTO public."DatosProceso_repetir"(repetir) VALUES ('una_vez');
         INSERT INTO public."DatosProceso_repetir"(repetir) VALUES ('cada_dia');
         INSERT INTO public."DatosProceso_repetir"(repetir) VALUES ('cada_semana');
         INSERT INTO public."DatosProceso_repetir"(repetir) VALUES ('cada_mes');
         INSERT INTO public."DatosProceso_repetir"(repetir) VALUES ('cada_año');""")
    conn                   = psycopg2.connect(config)
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit()
except:
    print('DATO REPETIO')



CAUSAS_TM = [
        'indefinido',
        'comida',
        'juntas',
        'mantenimiento_autonomo',
        'mantenimiento_preventivo',
        'capacitacion',
        'cambio_modelo',
        'falta_material',
        'falta_operador',
        'inspeccion',
        'correctivo_maquina',
        'falta _calibrador',
        'cambio_herramientas',
        'ajustes_proceso',
        'retrabajo',
        'desperdicio',
        'fin_de_ciclo',
        'recesos',
        'mantenimiento_planeado',
        'pruebas',
        'otros',
        'correctivo_herramienta',
        'flujo_bloqueado',
        'maquina_detenida',
        'maquina_en_espera_lista',
        'maquina_detenida_en_ciclo',
        'trabajando',
        'ciclo_terminado',
        'maquina_alarmada',
        "init_disponibilidad",
        "init_calidad",
        "init_eficiencia",
        "maquina_detenida_correctivo_ATC",
        "ajuste_de_programa",
        "maquina_detenida_puerta_de_atc_abierta",


        # Actualizacion Nuevas CausasTM.
        'Mtto_Prevent_Herrmt',
        'Falta_Herrmt',
        'Falta_Material',
        'Velocidad_Reducida',
        'Cambio_Herrmienta',
        'Ajuste_herramienta',
        'Causas_especiales_prod',
        'Pzt_scrap',
        'Inspeccion100',
         ]

#    DATOS_SIMILARES =  [
#        # Nombre_HRxHR            CausaTM                      Area
#        # Mtto  y Herm.
#        ['Mtto_Prevent_Herrmt'    ,''                        ,'mantenimiento'],
#        ['Falta_Herrmt'           ,''                        ,'mantenimiento'],
#        # Material
#        ['Falta_Material'         ,'falta_material'           ,''            ],
#        # Proceso
#        ['Velocidad_Reducida'     ,''                         ,''            ],
#        # Produccion.
#        ['Cambio_Herrmienta'      ,''                         , 'operaciones'],
#        ['Ajuste_herramienta'     ,''                         , 'operaciones'],
#        ['Causas_especiales_prod' ,''                         , 'operaciones'],
#        # Calidad
#        ['Pzt_scrap'              ,''                         ,     'calidad'],
#        ['Inspeccion100'          ,''                         ,     'calidad'],
#
#
#              ]


CAUSAS_TM = [
["indefinido",	                         False,	   4,	"930",	3,	4,	930],
["comida"	,                              True,	   2,	"830",	1,	3,	830],
["juntas"	,                              True,	   2,	"830",	1,	3,	830],
["mantenimiento_autonomo",	            True,     2,	"730",	1,	3,	730],
["mantenimiento_preventivo",	         True,	   2,	"630",	2,	3,	630],
["capacitacion"	,                       True,	   2,	"530",	2,	3,	530],
["cambio_modelo",	                     True,	   2,	"430",	1,	3,	430],
["falta_material",                      True,	   2,	"330",	2,	3,	330],
["falta_operador",                      True,	   3,	"130",	2,	2,	130],
["inspeccion",	                        True,	   2,	"30",	1,	3,	30],
["correctivo_maquina",	               True,	   3,	"920",	2,	2,	920],
["falta _calibrador",	                  True,	   2,	"820",	2,	3,	820],
["cambio_herramientas",	               True,	   2,	"720",	1,	3,	720],
["ajustes_proceso",                     False,	4,	"620",	3,	4,	620],
["retrabajo"	,                           True,   	2,	"520",	2,	3,	520],
["desperdicio",	                         False,	3,	"520",	1,	3,	520],
["fin_de_ciclo",	                       True,	1,	"420",	1,	3,	420],
["recesos",	                             True,	   2,	"320",	2,	3,	320],
["mantenimiento_planeado",	             True,	   2,	"220",	1,	3,	220],
["pruebas",                              True,	   2,	"120",	2,	3,	120],
["otros"                                 , False,	4,	"-10",	3,	4,	-10],
["correctivo_herramienta"                , True,	   3,	"950",	2,	3,	950],
["flujo_bloqueado"	                     ,True,    	2,	"750",	2,	3,	750],
["maquina_detenida"                      , True,	3,	"850",	2,	2,	850],
["maquina_en_espera_lista"               , True,	2,	"450",	2,	2,	450],
["maquina_detenida_en_ciclo"             , True,	3,	"-10",	2,	3,	600],
["trabajando"                            , True,	1,	"-10",	1,	1,	-10],
["ciclo_terminado"                       , True,	1,	"-10",	1,	3,	-10],
["maquina_alarmada"                      , True,	3,	"540",	2,	3,	540],
["init_disponibilidad"                   , False,	4,	"-10",	3,	4,	-10],
["init_calidad"                          , False,	4,	"-7",	3,	4,	-7],
["init_eficiencia"                       , False,	4,	"-6",	3,	4,	-6],
["maquina_detenida_correctivo_ATC"	     , True,	2,	"50",	1,	3,	50],
["ajuste_de_programa"                    , False,	4,	"-16",	3,	4,	1],
["maquina_detenida_puerta_de_atc_abierta", True,	2,	"100",2, 2,	-5],
["Mtto_Prevent_Herrmt"                   ,	False,	2,	"100",2, 2,	-501],
["Falta_Herrmt"                          ,	False,	2,	"100",2, 2,	-502],
["Falta_Material"                        ,	False,	2,	"100",2, 2,	-503],
["Velocidad_Reducida"                    ,	False,	2,	"100",2, 2,	-504],
["Cambio_Herrmienta"                     ,	False,	2,	"100",2, 2,	-505],
["Ajuste_herramienta"                    ,	False,	2,	"100",2, 2,	-506],
["Causas_especiales_prod"                ,	False,	2,	"100",2, 2,	-507],
["Pzt_scrap"                             ,	False,	2,	"100",2, 2,	-508],
["Inspeccion100"                         ,	False,	2,	"100",2, 2,	-509],
["restablecer_ctrZ"                      ,	False,	2,	"100",2, 2,	-510],
]


cursor = conn.cursor()
for i in CAUSAS_TM:
    try:
        QUERY   = ("""INSERT INTO public.gestion_causastm(
                   "CausasTm", "activarNotificacion", "colorAlerta_id", indicacion, "modoAlerta_id", sonido_id, indicacion_float)
                   VALUES ('"""+str(i[0])+"""', """+str(i[1])+""","""+str(i[2])+""",'"""+str(i[3])+"""', """+str(i[4])+""", """+str(i[5])+""", """+str(i[6])+""");""")

        conn   = psycopg2.connect(config)
        cursor = conn.cursor()
        cursor.execute(QUERY)
        conn.commit()
    except:
        print('DATO EXISTENTE')

#cursor = conn.cursor()
#for i in CAUSAS_TM:
#
#    QUERY = ("""INSERT INTO public.gestion_causastm(
#	            "CausasTm")
#	            VALUES ('"""+str(i)+"""');""")
#
#    cursor.execute(QUERY)
#    conn.commit()

##################################################################
# SEIS PERDIDAS..........
##################################################################

SEIS_PERDIDAS = [
       'paros_planeados',
       'paros_no_planeados',
       'retrabajo',
       'desperdicio',
       'NA']

for i in SEIS_PERDIDAS:

    try:
        QUERY = ("""INSERT INTO public.gestion_seisperdidas(
	               "SeisPerdidas")
	               VALUES ('"""+str(i)+"""');""")
        conn                   = psycopg2.connect(config)
        cursor = conn.cursor()
        cursor.execute(QUERY)
        conn.commit()
    except:
        print('DATO REPETIO')


##################################################################
# SCANNER_CODIGOS   ..........
##################################################################

SCANNER_CODIGOS = [
['990301',  'indefinido'],
['992631',	'maquina_alarmada'],
['992431'	,  'maquina_detenida'],
['992331',	'maquina_en_espera_lista'],
['992325',  'maquina_detenida_en_ciclo'],
['112345',	"comida"],
['112346',	"juntas"],
['112347',	"mantenimiento_autonomo"],
['212345',	"mantenimiento_preventivo"],
['112348',	"capacitacion"],
['112349',	"cambio_modelo"],
['412345',	"falta_material"],
['112340',	"falta_operador"],
['512345',	"inspeccion"],
['212346',	"correctivo_maquina"],
#['512346',	"falta_calibrador"],
['312345',	"cambio_herramientas"],
['112343',	"ajustes_proceso"],
['512348',	"retrabajo"],
['512349',	"desperdicio"],
['612345',	"fin_de_ciclo"],
['112342',	"recesos"],
['212347',	"mantenimiento_planeado"],
['512341',	"pruebas"],
['512347',	"otros"],
['312346',	"correctivo_herramienta"],
['312347',	"flujo_bloqueado"],
['51234856', 'ciclo_terminado'],
['990001',  'init_disponibilidad'],
['991051',  'init_calidad'],
['991061',  'init_eficiencia'],
['991071',  'maquina_detenida_correctivo_ATC'],
['991582',  'ajuste_de_programa'],
['9955523', 'maquina_detenida_puerta_de_atc_abierta'],
['9954621',	'trabajando'],

['1023932201','Mtto_Prevent_Herrmt'],
['1023932202','Falta_Herrmt'],
['10239322021','Falta_Material'],
['1023932203','Velocidad_Reducida'],
['1023932204','Ajuste_herramienta'],
['10239322014','Cambio_Herrmienta'],
['1023932205','Causas_especiales_prod'],
['1023932206','Pzt_scrap'],
['1023932207','Inspeccion100'],

['1023932208','restablecer_ctrZ'],

]





for i in SCANNER_CODIGOS:
    QUERY = ("""SELECT id
	             FROM public.gestion_causastm
                WHERE "CausasTm" = '"""+str(i[1])+"""'""")
    try:
        conn                   = psycopg2.connect(config)
        cursor = conn.cursor()
        cursor.execute(QUERY)
        conn.commit()

        for i2 in cursor:
            causasTm_id = i2[0]


        QUERY = ("""INSERT INTO public.gestion_scanner(
	             "codigoID", "CausasTm_id")
                 VALUES ("""+str(i[0])+""",'"""+str(causasTm_id)+"""');""")

        conn                   = psycopg2.connect(config)
        cursor = conn.cursor()
        cursor.execute(QUERY)
        conn.commit()
    except:
        print('DATO EXISTENTE')


##################################################################
# SCANNER_CODIGOS   ..........
##################################################################


DATOS = [
["disponibilidad",	"paros_planeados",    	"comida",                	 "operaciones"],
["disponibilidad",	"paros_planeados",   	"juntas",                	 "operaciones"],
["disponibilidad",	"paros_planeados",   	"mantenimiento_autonomo",	 "operaciones"],
["disponibilidad",	"paros_planeados",    	"mantenimiento_preventivo",	 "mantenimiento"],
["disponibilidad",	"paros_planeados",	    "capacitacion",	             "operaciones"],
["disponibilidad",	"paros_planeados",   	"cambio_modelo",          	 "manufactura"],
["disponibilidad",	"paros_no_planeados",	"falta_material",         	 "operaciones"],
["disponibilidad",	"paros_no_planeados",	"falta_operador",	         "operaciones"],
["disponibilidad",	"paros_no_planeados",	"inspeccion",            	 "calidad"],
["disponibilidad",	"paros_no_planeados",	"correctivo_maquina",	     "mantenimiento"],
["disponibilidad",	"paros_no_planeados",	"falta _calibrador",      	 "calidad"],
["disponibilidad",	"paros_no_planeados",	"cambio_herramientas",    	 "herramientas"],
["disponibilidad",	"paros_no_planeados",	"ajustes_proceso",        	 "manufactura"],
["calidad",	        "retrabajo",	        "retrabajo",             	 "calidad"],
["calidad",       	"desperdicio",	        "desperdicio",	             "calidad"],
["eficiencia",      "NA",	                "fin_de_ciclo",           	 "NA"],
["disponibilidad",	"paros_planeados",	    "otros",	                 "NA"],
["disponibilidad",	"paros_no_planeados",	"correctivo_herramienta",	 "herramientas"],
["disponibilidad",	"paros_no_planeados",	"flujo_bloqueado",	         "operaciones"],
["disponibilidad",	"paros_no_planeados",	"maquina_detenida",	         "NA"],
["disponibilidad",	"paros_no_planeados",	"maquina_en_espera_lista",	 "NA"],
["disponibilidad",	"paros_no_planeados",	"maquina_detenida_en_ciclo", "manufactura"],
["eficiencia",	    "NA",	                "trabajando",	             "NA"],
["eficiencia"	,   "NA",                   "ciclo_terminado",           "NA"],
["disponibilidad"	,"paros_no_planeados",  "maquina_alarmada",          "mantenimiento"],
["disponibilidad", 	"NA",                   "init_disponibilidad",	     "NA"],
["eficiencia",   	"NA",                  	"init_eficiencia",      	 "NA"],
["calidad",	        "NA",                	"init_calidad",          	 "NA"],
["NA",            	"NA",                	"indefinido",            	 "NA"],


["NA",            	"paros_planeados",     	"Mtto_Prevent_Herrmt",       "manufactura"],
["NA",            	"paros_no_planeados",   "Falta_Herrmt",            	 "herramientas"],
["NA",            	"paros_no_planeados",   "Falta_Material",            "materiales"],
["NA",            	"paros_no_planeados",   "Velocidad_Reducida",        "manufactura"],
["NA",            	"paros_no_planeados",   "Cambio_Herrmienta",         "herramientas"],
["NA",            	"paros_planeados",      "Ajuste_herramienta",        "manufactura"],
["NA",            	"paros_no_planeados",   "Causas_especiales_prod",    "NA"        ],
["NA",            	"paros_no_planeados",   "Pzt_scrap",                 "calidad"],
["NA",            	"paros_no_planeados",   "Inspeccion100",             "calidad"],

["NA",            	"NA",                   "restablecer_ctrZ",          "NA"],

]


#QUERY = ("""DELETE FROM public.gestion_causastm""")
#cursor = conn.cursor()
#cursor.execute(QUERY)
#conn.commit()


for i in DATOS:
    try:
        cursor = conn.cursor()
        QUERY = ("""SELECT id
	                FROM public.gestion_clasificacionete
                   WHERE "clasificacionEte" = '"""+str(i[0])+"""'""")
        conn                   = psycopg2.connect(config)
        cursor.execute(QUERY)
        conn.commit()
        clasificacionEte_id = 1000

        for i2 in cursor:
            clasificacionEte_id = i2[0]

        cursor = conn.cursor()
        QUERY = ("""SELECT id
	                FROM public.gestion_seisperdidas
                    WHERE "SeisPerdidas" = '"""+str(i[1])+"""'""")
        conn                   = psycopg2.connect(config)

        cursor.execute(QUERY)
        conn.commit()
        SeisPerdidas_id = 1000

        for i3 in cursor:
            SeisPerdidas_id = i3[0]

        cursor = conn.cursor()
        CausasTm_id =1000
        QUERY = ("""SELECT id
	                FROM public.gestion_causastm
                    WHERE "CausasTm" = '"""+str(i[2])+"""'""")
        conn                   = psycopg2.connect(config)
        cursor.execute(QUERY)
        conn.commit()
        for i4 in cursor:
            CausasTm_id = i4[0]



        QUERY = ("""SELECT id
	                FROM public.gestion_areas
                    WHERE areas = '"""+str(i[3])+"""'""")
        conn                   = psycopg2.connect(config)
        cursor = conn.cursor()
        cursor.execute(QUERY)
        conn.commit()
        areas_id = 1000
        for i5 in cursor:
            areas_id = i5[0]


        QUERY = ("""INSERT INTO public.gestion_gestionete(
	    	"CausasTm_id", "SeisPerdidas_id", areas_id, "clasificacionEte_id")
	    	VALUES ("""+str(CausasTm_id)+""", """+str(SeisPerdidas_id)+""", """+str(areas_id)+""", """+str(clasificacionEte_id)+""")""")

        conn                   = psycopg2.connect(config)
        cursor = conn.cursor()
        cursor.execute(QUERY)
        conn.commit()
    except:
        print('datos repetidos')

print('INSERTADO DATOS POR DEFECTO EN: public.gestion_gestionete')

#------------------------DATOS DEMO -------------------------------------------
try:
    QUERY = ("""INSERT INTO public."opcionesGenerales_marcamaquina"(
	            "MarcaMaquina")
	             VALUES ('Marca_Prueba');""")
    conn                   = psycopg2.connect(config)
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit()
    print('INSERTADO DATOS POR DEFECTO EN: public."opcionesGenerales_marcamaquina"')
except:
    print('DATO REPETIO')

try:
    QUERY = ("""INSERT INTO public."opcionesGenerales_modelosmaquinas"(
              	"ModelosMaquinas", "MarcaMaquina_id")
    	         VALUES ('MarcaMaquina',(SELECT id
                FROM public."opcionesGenerales_marcamaquina"
                WHERE ("MarcaMaquina" = 'Marca_Prueba')))""")

    print('INSERTADO DATOS POR DEFECTO EN: public."opcionesGenerales_modelosmaquina"')
    conn                   = psycopg2.connect(config)
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit()
except:
    print('DATO REPETIDO')

A = 1
try:

    QUERY = ("""INSERT INTO public.disponibilidad_datosmaquinaete(
                "tiempoDisponibleMaquina", empresa_id, linea_id, maquina_id, planta_id, "piezasProgramadas", "tiempoCicloEstandar", componente)
                 VALUES (8,(SELECT id
                 FROM public."DatosEmpresa_empresa"
                 WHERE (empresa = 'EMPRESA_DEMO') LIMIT 1),(SELECT id
                 FROM public."DatosEmpresa_linea"
                 WHERE (linea = 'LINEA_DEMO') LIMIT 1),(SELECT id
                 FROM public."DatosEmpresa_maquina"
                 WHERE (maquina = 'MAQUINA_DEMO') LIMIT 1),(SELECT id
                 FROM public."DatosEmpresa_planta"
                 WHERE (planta = 'PLANTA_DEMO') LIMIT 1), 40, 223,'caja2105');""")

    print(QUERY)

    conn                   = psycopg2.connect(config)
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit()

    print('INSERTADO DATOS POR DEFECTO EN: public.disponibilidad_datosmaquinaete"')


except:
    print('DATO REPETIDO')

try:
    QUERY = ("""INSERT INTO public."opcionesGenerales_opcionesgenerales"(
    	        "Activar_Ete_Variable", "Contemplar_solo_paros_Programados", "Filtrar_por_componente", "Tiempo_transcurrido")
              	VALUES (True, False, False, 0.0);""")

    print('INSERTADO DATOS POR DEFECTO EN: public."opcionesGenerales_opcionesgenerales"')

    conn                   = psycopg2.connect(config)
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit()
except:
    print('DATO REPETIDO')

try:

    QUERY = ("""INSERT INTO public."opcionesGenerales_prioridad"(
                "Prioridad") VALUES (1);
                 INSERT INTO public."opcionesGenerales_prioridad"(
                "Prioridad") VALUES (2);
                 INSERT INTO public."opcionesGenerales_prioridad"(
                "Prioridad") VALUES (3);""")
    conn                   = psycopg2.connect(config)
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit()
    print('INSERTADO DATOS POR DEFECTO EN: public."opcionesGenerales_prioridad"')
except:
    print('DATO REPETIDO')

try:

    QUERY = ("""INSERT INTO public."opcionesGenerales_tipodetarea" ("TipoDeTarea") VALUES ('MANTENIMIENTO');
                INSERT INTO public."opcionesGenerales_tipodetarea" ("TipoDeTarea") VALUES ('REPORTES');
                INSERT INTO public."opcionesGenerales_tipodetarea" ("TipoDeTarea") VALUES ('ANALITCIA');
                INSERT INTO public."opcionesGenerales_tipodetarea" ("TipoDeTarea") VALUES ('INICIALIZANDO');
                INSERT INTO public."opcionesGenerales_tipodetarea" ("TipoDeTarea") VALUES ('PRUEBA');
                INSERT INTO public."opcionesGenerales_tipodetarea" ("TipoDeTarea") VALUES ('MANEJO_DE_DATOS');""")

    conn                   = psycopg2.connect(config)
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit()
except:
    print('DATO REPETIDO')

try:
    QUERY = ("""INSERT INTO public."opcionesGenerales_estado"("Estado") VALUES ('EN_ESPERA');
                INSERT INTO public."opcionesGenerales_estado"("Estado") VALUES ('RUN');
                INSERT INTO public."opcionesGenerales_estado"("Estado") VALUES ('ERROR');
                INSERT INTO public."opcionesGenerales_estado"("Estado") VALUES ('EJECUTADO');""")
    conn                   = psycopg2.connect(config)
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit()
except:
    print('DATO REPETIDO')

DATOS = [
['ACTIVE'      ,'AUTOMATIC'         ,'_1_CYCLE_STOP'              ,'maquina_detenida_en_ciclo'              ,'-10','3'],
['ACTIVE'      ,'AUTOMATIC'         ,'_ALARM'                     ,'ciclo_terminado'                       ,'-10','1'],
['ACTIVE'      ,'AUTOMATIC'         ,'_ALARM'                     ,'trabajando'                            ,'-10','1'],
['ACTIVE'      ,'AUTOMATIC'         ,'0'                          ,'ciclo_terminado'                       ,'-10','1'],
['ACTIVE'      ,'AUTOMATIC'         ,'0'                          ,'trabajando'                            ,'-10','1'],
['0'           ,'AUTOMATIC'         ,'0'                          ,'ciclo_terminado'                       ,'-10','1'],
['0'           ,'AUTOMATIC'         ,'0'                          ,'trabajando'                            ,'-10','1'],
['READY'       ,'AUTOMATIC'         ,'0'                          ,'maquina_en_espera_lista'               ,'-10','3'],
['STOPPED'     ,'MANUAL'            ,'0'                          ,'maquina_detenida'                      ,'-10','3'],
['STOPPED'     ,'AUTOMATIC'         ,'0'                          ,'maquina_detenida'                      ,'-10','3'],
['FEED_HOLD'   ,'AUTOMATIC'         ,'0'                          ,'maquina_detenida'                      ,'-10','3'],
['ACTIVE'      ,'AUTOMATIC'         ,'MAGAZINE_DOOR_OPENED'       ,'maquina_detenida_puerta_de_atc_abierta','-10','3'],
['READY'       ,'MANUAL_DATA_INPUT' ,'0'                          ,'ajuste_de_programa'                    ,'-10','3'],
['ACTIVE'      ,'AUTOMATIC'         ,'_ARM_POSITION_MALF.'        ,'maquina_detenida_correctivo_ATC'       ,'-10','3'],
['INTERRUPTED' ,'AUTOMATIC'         ,'0'                          ,'maquina_detenida_en_ciclo'             ,'-10','3'],
['_ALARM'      ,'INTERRUPTED'       ,'AUTOMATIC'                  ,'maquina_alarmada'                      ,'-10','3']]

#server_postgres        =[IP,PUERTO,DB,USER,PASSWORD] # Conexion Postgres
#config                 = "host= "+ server_postgres[0] + " port="+ server_postgres[1]+  " dbname="+server_postgres[2]+ " user="+server_postgres[3]+ " password="+server_postgres[4]
#conn                   = psycopg2.connect(config)

for i in DATOS:

    QUERY = ("""INSERT INTO public."opcionesGenerales_variablesdelcontrol"("MarcaMaquina_id", "ModelosMaquinas_id", "Execution", "Modo", "Alarma", "CausasTM_id", "Prioridad_id", indicacion,"CorteViruta")
        VALUES ((SELECT id FROM public."opcionesGenerales_marcamaquina" WHERE "MarcaMaquina" = 'Marca_Prueba'), (SELECT id FROM public."opcionesGenerales_modelosmaquinas" WHERE "ModelosMaquinas" = 'Modelo_Prueba'),
                 '"""+str(i[0])+"""','"""+str(i[1])+"""','"""+str(i[2])+"""',(SELECT id FROM public.gestion_causastm WHERE "CausasTm" = '"""+str(i[3])+"""'),
                 (SELECT id FROM public."opcionesGenerales_prioridad" WHERE "Prioridad" = '"""+str(i[5])+"""'),
                 '"""+str(i[4])+"""', False);""")
#    print '---------------'
#    print(QUERY)
#    print '---------------'

    try:
        conn                   = psycopg2.connect(config)
        cursor = conn.cursor()
        cursor.execute(QUERY)
        conn.commit()
    except:
        print('ERROR C')


try:
    QUERY = ("""INSERT INTO public."DatosProceso_datosoperador"(
	         "NoNomina", "Comentario", maquina_id, "NivelMultiHabilidad")
	          VALUES  ('00001010', 'OPERADOR INDEFINIDO', 1, 0);""")
    conn                   = psycopg2.connect(config)
    cursor = conn.cursor()
    cursor.execute(QUERY)
    conn.commit()
except:
    print('ERROR ')


insert_variables_de_control_por_default(config)

conn.close()
