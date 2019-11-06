#from django.http import HttpResponse

from   datetime              import datetime
import psycopg2

from   .conexiones_bases_datos import get_buffer_scanner_data
#from   .conexiones_bases_datos import get_data_base
from   .get_data_base          import get_data_base
from django.http import HttpResponse
import json
import time

def hello_world(request):
    return HttpResponse('Oh, hi! Current server time is {now}')

# Insertar datos en el buffer mediante URL
def insert_buffer_data(request,maquina,causaTM):

#    maquina = request.GET['maquina']
#    causaTM = request.GET['causaTM']
    fecha   = datetime.now()
    try:
        IP,PUERTO,DB,USER,PASSWORD = get_data_base('/DJANGO/mtc_etedjmodel')
    except:
        IP,PUERTO,DB,USER,PASSWORD = get_data_base('/modelos_django01/mt_connect_app_dj/')

    server_postgres        = [IP,PUERTO,DB,USER,PASSWORD]
    config                 = "host= "+ server_postgres[0] + " port="+ server_postgres[1]+  " dbname="+server_postgres[2]+ " user="+server_postgres[3]+ " password="+server_postgres[4]
    conn                   = psycopg2.connect(config)
    data_all               = True

    if causaTM == 'ciclo_terminado':
        CAUSAtm = ['trabajando','ciclo_terminado']
    else:
        CAUSAtm = [causaTM]
    print('-------------------::',CAUSAtm)
    noevent     = 0
    for i in range(0,len(CAUSAtm),1):
        noevent = noevent +1

        if noevent == 1:
            time.sleep(1)

        causaTM = str(CAUSAtm[i])
        # Insertar en el buffer de datos.
        mac_adress,causasTM_id,codigo,Prioridad_id,Prioridad,indicacion,ERROR   = get_buffer_scanner_data(conn,maquina,causaTM)
        print('-----------------  causaTM:',causaTM)

        if ERROR == '':
            QUERY = ("""INSERT INTO public.gestion_scannerbuffer(
    	             fecha, codigo, mac_adress, indicacion, prioridad)
    	             VALUES ('"""+str(fecha)+"""','"""+str(codigo)+"""' , '"""+str(mac_adress)+"""', '"""+str(indicacion)+"""', """+str(Prioridad)+""");""")

            cursor = conn.cursor()
            cursor.execute(QUERY)
            conn.commit()

    conn.close()

    data = {'no_event':noevent,
            'mac_adress':mac_adress,
            'causasTM_id':causasTM_id,
            'codigo':codigo,
            'Prioridad_id':Prioridad_id,
            'Prioridad':Prioridad,
            'indicacion':indicacion,
            'ERROR':ERROR,
            }

    return HttpResponse(
            json.dumps(data,indent=4),
            content_type='application/json')


#maquina = 'MAQUINA_DEMO'
#causaTM = 'maquina_alarmada'
#insert_buffer_data(maquina,causaTM)
