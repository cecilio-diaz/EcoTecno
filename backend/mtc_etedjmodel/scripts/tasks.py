from   __future__ import absolute_import, unicode_literals
from   scripts.task_dumpdata import backup_config
from   celery.decorators import task
from   project.celery import app as celery_app

@task(name="backup_config")
def backup_config():

    os.system('python manage.py dumpdata auth.user           > backups/user.yaml')
    print('BACKUP USERS                            : OK')
    os.system('python manage.py dumpdata opcionesGenerales   > backups/opcionesGeneralesbackup_maquinas.yaml')
    print('BACKUP opcionesGeneralesbackup_maquinas : OK')
    os.system('python manage.py dumpdata DatosEmpresa        > backups/maquinas.yaml')
    print('BACKUP maquinas                         : OK')
    os.system('python manage.py dumpdata DatosProceso        > backups/DatosProceso.yaml')
    print('BACKUP DatosProceso                     : OK')
    os.system('python manage.py dumpdata estado_paros_enca   > backups/estado_paros_enca.yaml')
    print('BACKUP estado_paros_enca                : OK')
    os.system('python manage.py dumpdata estado_paros_deta   > backups/estado_paros_deta.yaml')
    print('BACKUP estado_paros_deta                : OK')
    os.system('python manage.py dumpdata estado_paros_deta2   > backups/estado_paros_deta2.yaml')
    print('BACKUP estado_paros_deta2               : OK')
    os.system('python manage.py dumpdata estado_paros_deta3   > backups/estado_paros_deta3.yaml')
    print('BACKUP estado_paros_deta3               : OK')
    os.system('python manage.py dumpdata RegistroParo        > backups/RegistroParo.yaml')
    print('BACKUP RegistroParo                     : OK')
