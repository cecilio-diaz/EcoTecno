from __future__ import absolute_import, unicode_literals
from celery     import shared_task
from datetime import datetime, time, timedelta


from apps.historial.get_no_turno    import get_no_turno
# Modelos

from apps.DatosEmpresa.models         import maquina
from apps.ciclos.models               import conteo
from apps.historial.get_no_turno      import get_no_turno
from apps.historial.models            import estados_inicial
from apps.programa.models             import cnc
from apps.programa.models             import modelo_de_pieza

#from   apps.DatosEmpresa.models       import maquina


# @shared_task(name = "clc_ciclos_y_conexion_hxh")
def get_maquina():
    maquina2 = maquina.objects.all()
    maquina2 = maquina2.values()

    maquina2 = maquina2[0]
    maquina2 = maquina2['maquina']

    print(maquina2)

    return maquina2

@shared_task(name = "get_conteo_ciclos")
def get_conteo_ciclos():

    maquina2 = maquina.objects.all()
    maquina2 = maquina2.values()

    ciclos_terminados_turno = 0
    ciclos_terminados_hora  = 0
    for i in maquina2:

        maquina_id          = int(i['id'])
        maquina_i           = i['maquina']

        fecha_now = datetime.now()
        turno2,fecha_turno  = get_no_turno(fecha_now)
        fecha_hora          = datetime(fecha_now.year, fecha_now.month, fecha_now.day, fecha_now.hour)

        # PRUEBA
        # OBTENER LOS PROGRAMAS EJECUTADOS EN ESA FECHA

        datos_turno    = estados_inicial.objects.filter(maquina=maquina_id,piezas=1,fecha__range=[fecha_turno,fecha_now])
        datos_turno    = datos_turno.values()
        programa_cnc   = []

        for datos_i in datos_turno:
            programa_cnc_i = datos_i['programa_cnc_id']

            if  programa_cnc_i not in programa_cnc:
                programa_cnc.append(programa_cnc_i)

        # // OBTENER LOS PROGRAMAS EJECUTADOS EN ESA FECHA

       #   CALCULAR CICLOS TERMINADOS EN EL TRURNO
        for programa_cnc_i in programa_cnc:

            ciclos_terminados_turno    = estados_inicial.objects.filter(programa_cnc_id=programa_cnc_i,maquina=maquina_id,piezas=1,fecha__range=[fecha_turno,fecha_now]).count()
            ciclos_terminados_hora     = estados_inicial.objects.filter(programa_cnc_id=programa_cnc_i,maquina=maquina_id,piezas=1,fecha__range=[fecha_hora,fecha_now]).count()

            print('ciclos_terminados_turno: ',ciclos_terminados_turno)
            print('ciclos_terminados_hora: ' ,ciclos_terminados_hora)

            if ciclos_terminados_hora > 0:

                datos  = estados_inicial.objects.filter(maquina=maquina_id,piezas=1,fecha__range=[fecha_turno,fecha_now]).order_by('-id')
                datos  = datos.values()

                for i2 in datos:
                    programa_cnc_id  = i2['programa_cnc_id']

                # VERIFICAR QUE EL CAMPO EXISTA (PARA NO INSERTAR DATOS DUPLICADOS).
                cont  = conteo.objects.filter(maquina_id=maquina_id,programa_cnc_id=programa_cnc_id,FechaTurno=fecha_turno).order_by('-id')
                data = cont.values()

                print('-----------------------------------------------')
                print('data:',data)
                print('len(data) ',len(data))
                print('-----------------------------------------------')

                print(data)
                print(type(data))

                try:
                    data            = data[0]
                    programa_cnc_id = data['programa_cnc_id']
                    turno           = data['turno']
                    ciclo_turno     = data['ciclo_turno']
                    ciclo_hora      = data['ciclo_hora']

                    print('maquina_id %2s |programa_cnc_id %2s | ciclo_turno_old: %3s | ciclo_turno_new: %3s | ciclo_hora_new %2s| ciclo_hora_old %2s' %(str(maquina_id),str(programa_cnc_id),str(ciclo_turno),str(ciclos_terminados_turno),str(ciclo_hora),str(ciclos_terminados_turno)))
                except:
                    print('Inicializando _datos_')

                INSERT_PIEZA_NUEVA = False
                if len(data) == 0: # Inicializando Datos.
                    INSERT_PIEZA_NUEVA = True
                    print('INSERTAR DATOS INICIALES. ')
                    # Insertar datos por primera vez
                    cont = conteo.objects.create(maquina_id=maquina_id,programa_cnc_id=programa_cnc_id,ciclo_hora=ciclos_terminados_hora,ciclo_turno=ciclos_terminados_turno,compensacion_resta=0,compensacion_suma=0)
                    cont.save()

                else:
                    if ciclo_turno != ciclos_terminados_turno or ciclo_hora != ciclos_terminados_turno:
                        INSERT_PIEZA_NUEVA = True
                        print('ACTUALIZANDO CICLOS')
                        cont = conteo.objects.filter(maquina_id=maquina_id,programa_cnc_id=programa_cnc_id,FechaTurno=fecha_turno).update(ciclo_hora=ciclos_terminados_hora,ciclo_turno=ciclos_terminados_turno)
                        print('***9***9***9')
                        print(cont)
                    else:
                        print('DATOS EXISTENTES')

                print('INSERT_PIEZA_NUEVA:',INSERT_PIEZA_NUEVA)

                # INSERTAR DATOS EN EL HXH.....
                # API. http://sam-rdsdev:9015/api/v1/registros/
                # VERIFICAR QUE NO SEA UN MODELO DESCONOCIDO.

                if INSERT_PIEZA_NUEVA == True:
                    datos_cnc = cnc.objects.filter(id=programa_cnc_id).values()[0]
                    nombre_de_pieza    = datos_cnc['nombre']
                    modelo_de_pieza_id = datos_cnc['modelo_de_pieza_id']

                    print()

                    nombre_de_pieza = modelo_de_pieza.objects.filter(id=modelo_de_pieza_id).values()[0]['nombre']

                    if nombre_de_pieza != 'MODELO_DESCONOCIDO':
                        print(nombre_de_pieza)


    return ciclos_terminados_turno
