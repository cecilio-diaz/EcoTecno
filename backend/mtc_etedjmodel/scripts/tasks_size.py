from __future__ import absolute_import, unicode_literals
from celery     import shared_task
import sys
from   apps.datos.models        import dato
from   apps.DatosEmpresa.models import maquina
import numpy as np

from datetime import datetime, time, timedelta

@shared_task(name = "delete_exceso_data")
def get_size_datos():

    maquinas = maquina.objects.all().values()
    all_size = 0

    Megas_por_maquina = []
    for maq in maquinas:

        ID              = maq['id']
        maquina_name    = maq['maquina']
        db_size_mb      = maq['db_size_mb']

        MyModel     = dato.objects.filter(maquina_id=ID).values()
        count_t     = MyModel.count()
        coeficiente = sys.getsizeof(MyModel)
        total_size  = sys.getsizeof(MyModel) * MyModel.count()
        total_size  = total_size/1000000

        # Eliminar datos redundantes............................................
        delete_data       = False
        d_delete          = 0.0
        registros_optimos = 0.0

        N_D = 10   # Numero de ciclos for .
        NDD = 5000  # Lista de datos a eliminar
        contador_delete = 0
        if total_size > db_size_mb:

            while total_size > db_size_mb:
                MyModel     = dato.objects.filter(maquina_id=ID).values()
                count_t     = MyModel.count()
                coeficiente = sys.getsizeof(MyModel)
                total_size  = sys.getsizeof(MyModel) * MyModel.count()
                total_size  = total_size/1000000

                delete_data        = True
                d_delete           = total_size-db_size_mb
                registros_optimos  = (db_size_mb*count_t)/total_size

                registros_optimos  = int(np.round(registros_optimos))

                registros_eliminar = count_t - registros_optimos

                D = dato.objects.filter(maquina_id=ID).values().order_by('id')[0]
                ID_delete = D['id']

                D = dato.objects.filter(id=ID_delete).delete()
                dato.objects.filter(maquina_id=ID,id__range=[ID_delete,ID_delete+registros_eliminar+1000]).delete()
                ID_delete = ID_delete+NDD

                print('maquina: %20s |total_size [mb]: %10s| maximo_posible [mb]: %3s|delete_data: %5s| No_d: %10s|eliminar:%4.2f|e_reg: %5.2f| '%(maquina_name,str(total_size),str(db_size_mb),delete_data,count_t,d_delete,registros_optimos))
        print('maquina: %20s |total_size [mb]: %10s| maximo_posible [mb]: %3s|delete_data: %5s| No_d: %10s|eliminar:%4.2f|e_reg: %5.2f| '%(maquina_name,str(total_size),str(db_size_mb),delete_data,count_t,d_delete,registros_optimos))
        all_size = all_size + total_size
        Megas_por_maquina.append(total_size)
    print('FULL SIZE: ',all_size)

    return Megas_por_maquina
