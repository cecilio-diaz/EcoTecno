import   psycopg2
from     datetime                                       import datetime, time, timedelta
import   time
import   os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","mt_connect_app_dj.settings")
import django
#django.setup()
from apps.DatosEmpresa.models import empresa

def insert_auto_empresa(nombre):
    nombre_empresa = nombre + '1112-'
    empresa_name = empresa.objects.get_or_create(empresa=nombre_empresa)[0]
    todas_las_empresas = empresa.objects.all()
    print(todas_las_empresas)
    empresa_name.save()
    print("GUARDANDO NOMBRE DE EMPRESA IGUAL A:",nombre_empresa)
#if __name__ == '__main__':
#    print('Insertando datos')
#    insert_auto_empresa()
