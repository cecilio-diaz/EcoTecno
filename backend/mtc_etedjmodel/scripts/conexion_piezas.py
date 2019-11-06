from __future__   import absolute_import, unicode_literals
from   celery     import shared_task
import sys
import numpy as np
from   apps.datos.models        import dato
from   apps.DatosEmpresa.models import maquina
