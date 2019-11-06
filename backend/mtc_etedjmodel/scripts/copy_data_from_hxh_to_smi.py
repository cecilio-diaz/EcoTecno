import requests
import json

# CONFIGURACION DE LAS APIS.

apis = {'paros_anca_hxh'        :'http://sam-rdsdev:9015/api/v1/paros_enca',
        'estado_paros_enca_smi' :'http://localhost:8000/api/v1/estado_paros_enca/',
        'paros_deta'            :'http://sam-rdsdev:9015/api/v1/paros_deta/',
        'estado_paros_deta'     :'http://localhost:8000/api/v1/estado_paros_deta/',
        'paros_deta2'           :'http://sam-rdsdev:9015/api/v1/paros_deta2/',
        'estado_paros_deta2'    :'http://localhost:8000/api/v1/estado_paros_deta2/',
        }




# DESCIPCION: ESTA FUNCION ES PARA LEER EL DATO INSERTADO EN EL HxH he incorporarlo en
# el smi.

def insert_update_data_from_hxh_to_smi(apis):

    data_hxh  = requests.get(apis['paros_anca_hxh'])
    data_hxh  = data_hxh.json()

    for i in data_hxh:

        nombre =  i['nombre']
        ID_hxh     =  i['id']
        url_find_smi = apis['estado_paros_enca_smi'] +'?nombre='+nombre

        data_smi  = requests.get(url_find_smi)
        data_smi = data_smi.json()

        results =  data_smi['results']

        obj_smi = {
                  "nombre": nombre,
                  "ID_paros_enca": ID_hxh
                      }

        if len(results) == 0: # SI NO EXISTE
            print('INSERTANDO DATOS POR PRIMERA VEZ')
            solicitud = requests.post(apis['estado_paros_enca_smi'] , data = obj_smi)
        else:
            print('')
            print('CODIGO DE UPDATE PENDIENTE POR PROGRAMAR')
            print('')

# EJECUTAR LA COPIA DE LOS DATOS.




def copy_paros_deta(apis):

    data_hxh  = requests.get(apis['paros_deta'])
    data_hxh = data_hxh.json()

    for i in data_hxh:
        print(i)
        nombre           =  i['nombre']
        paro_enca_nombre = i['paro_enca_nombre']
        print(nombre)
        ID_hxh     =  i['id']

        url_find_smi = apis['estado_paros_deta'] +'?nombre='+nombre

        data_smi  = requests.get(url_find_smi)
        data_smi = data_smi.json()

        results =  data_smi['results']

        print(results)


        if len(results) == 0: # SI NO EXISTE

            # BUSCAR EL ID

            url_enca_data    = apis['estado_paros_enca_smi']+'?nombre='+paro_enca_nombre
            data_smi_enca    = requests.get(url_enca_data)
            data_smi_enca    = data_smi_enca.json()
            data_smi_enca    = data_smi_enca['results']
            data_smi_enca    = data_smi_enca[0]
            data_smi_enca_id = data_smi_enca['id']
            # // BUSCAR EL ID

            obj_smi =         {
                "nombre": nombre,
                "paro_enca": data_smi_enca_id,
                "ID_paros_deta": ID_hxh
            }

            print('INSERTANDO DATOS POR PRIMERA VEZ')
            solicitud = requests.post(apis['estado_paros_deta'] , data = obj_smi)

        else:
            print('')
            print('CODIGO DE UPDATE PENDIENTE POR PROGRAMAR')
            print('')

# DESCIPCION: ESTA FUNCION ES PARA LEER EL DATO INSERTADO EN EL HxH he incorporarlo en
# el smi.


def copy_paros_deta2(apis):

    data_hxh  = requests.get(apis['paros_deta2'])
    data_hxh = data_hxh.json()

    for i in data_hxh:
#        print i
        nombre           =  i['nombre']
        paro_enca_nombre =  i['paro_deta_nombre']
#        print nombre
        ID_hxh     =  i['id']

        url_find_smi = apis['estado_paros_deta2'] +'?nombre='+nombre

        data_smi  = requests.get(url_find_smi)
        data_smi = data_smi.json()

        results =  data_smi['results']

        if len(results) == 0: # SI NO EXISTE
#            print('INSERTANDO DATOS POR PRIMERA VEZ')
#            # BUSCAR EL ID

            url_enca_data  = apis['estado_paros_deta']+'?nombre='+paro_enca_nombre

            data_smi_enca  = requests.get(url_enca_data)
            data_smi_enca  = data_smi_enca.json()
            data_smi_enca  = data_smi_enca['results']
            data_smi_enca  = data_smi_enca[0]
            data_smi_enca_id = data_smi_enca['id']
#            print data_smi_enca_id
            # // BUSCAR EL ID



            obj_smi =         {
                   "nombre": nombre,
                   "paros_deta": data_smi_enca_id,
                   "ID_paros_deta2": ID_hxh
                                }
            print(obj_smi)

            solicitud = requests.post(apis['estado_paros_deta2'] , data = obj_smi)

insert_update_data_from_hxh_to_smi(apis)
copy_paros_deta(apis)
copy_paros_deta2(apis)
