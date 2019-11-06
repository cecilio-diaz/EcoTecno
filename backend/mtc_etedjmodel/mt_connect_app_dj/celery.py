from __future__       import absolute_import, unicode_literals
import os
from celery           import Celery
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mt_connect_app_dj.settings')

app = Celery('mt_connect_app_dj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
   # from mt_connect_app_dj.tasks_maquina import get_conteo_ciclos
    'get_conteo_ciclos (10s)': {  #name of the scheduler
        'task': 'get_conteo_ciclos',  # task name which we have created in tasks.py
        'schedule': 10.0,  # set the period of running
         'args': ()  # set the args
    },

    # from backups.tasks import backup_config
    'backup_config (60.0s)': {                  # name of the scheduler
        'task': 'backup_config',                # task name which we have created in tasks.py
        'schedule': 3600.0, # set the period of running
        'args': ()                             # set the args
    },

        # from apps.piezas.tasks import find_new_pieces
    'find_new_pieces (20.0s)': {                  # name of the scheduler
        'task': 'find_new_pieces',                # task name which we have created in tasks.py
        'schedule': 20.0, # set the period of running
        'args': ()                             # set the args
    },

    # from machine_services.tasks import get_data_mtconnect
    'get_data_mtconnect (10.0s)': {                 # name of the scheduler
        'task': 'get_data_mtconnect',                 # task name which we have created in tasks.py
        'schedule': 10.0,                          # set the period of running
        'args': ()                                 # set the args
    },

    # from scripts.tasks_size import get_size_datos
    'get_data_mtconnect (10.0s)': {                             # name of the scheduler
        'task': 'delete_exceso_data',                           # task name which we have created in tasks.py
        'schedule': crontab(hour=1, minute=30, day_of_week=1),  # set the period of running
        'args': ()                                 # set the args
    },
}
