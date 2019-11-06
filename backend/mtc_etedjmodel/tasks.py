#from __future__                       import absolute_import, unicode_literals
#from celery.decorators                import task
#from datetime                         import datetime, date
#from   datetime                       import datetime, time, timedelta
#from django.utils                     import timezone
#from   celery.decorators import task
#
#import os
#from   apps.historial.models          import estados_inicial
#
#from   apps.ciclos.models             import conteo
#from   apps.historial.get_no_turno    import get_no_turno
#from   apps.DatosEmpresa.models       import maquina
#
###@task(name="get_conteo_ciclos")
def get_conteo_ciclos():
    maquina =  maquina.objects.all().order_by('-id')
    maquina =  maquina.values()


    ciclos_terminados_turno = 0
    ciclos_terminados_hora  = 0
    for i in maquina3:
        maquina_id          = int(i['id'])
        maquina             = i['maquina']

        fecha_now           = datetime.now()
        turno2,fecha_turno  = get_no_turno(fecha_now)
        fecha_hora          = datetime(fecha_now.year, fecha_now.month, fecha_now.day, fecha_now.hour)

    #   CALCULAR CICLOS TERMINADOS EN EL TRURNO

        ciclos_terminados_turno    = estados_inicial.objects.filter(maquina=maquina_id,piezas=1,fecha__range=[fecha_turno,fecha_now]).count()
        ciclos_terminados_hora     = estados_inicial.objects.filter(maquina=maquina_id,piezas=1,fecha__range=[fecha_hora,fecha_now]).count()

        print('ciclos_terminados_turno: ',ciclos_terminados_turno)
        print('ciclos_terminados_hora: ',ciclos_terminados_hora)

        if ciclos_terminados_turno > 0:

            datos  = estados_inicial.objects.filter(maquina=maquina_id,piezas=1,fecha__range=[fecha_turno,fecha_now]).order_by('-id')
            datos  = datos.values()
            for i2 in datos:
                programa_cnc_id  = i2['programa_cnc_id']


            # VERIFICAR QUE EL CAMPO EXISTA (PARA NO INSERTAR DATOS DUPLICADOS).
            cont  = conteo.objects.filter(maquina_id=maquina_id,programa_cnc_id=programa_cnc_id,FechaTurno=fecha_turno).order_by('-id')
            data = cont.values()
            print(len(data) == 0)

            if len(data) == 0:
                print('INSERTAR DATOS INICIALES. ')
                # Insertar datos por primera vez
                cont = conteo.objects.create(maquina_id=maquina_id,programa_cnc_id=programa_cnc_id,ciclo_hora=ciclos_terminados_hora,ciclo_turno=ciclos_terminados_turno,compensacion_resta=0,compensacion_suma=0)
                cont.save()
            else:
                print('ACTUALIZANDO CICLOS')
                cont = conteo.objects.filter(maquina_id=maquina_id,programa_cnc_id=programa_cnc_id,FechaTurno=fecha_turno).update(ciclo_hora=ciclos_terminados_hora,ciclo_turno=ciclos_terminados_turno,compensacion_resta=0,compensacion_suma=0)

    return ciclos_terminados_turno
