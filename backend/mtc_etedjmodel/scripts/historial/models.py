from django.db                      import models
from apps.DatosEmpresa.models       import maquina
from django.utils                   import timezone
from apps.gestion.models            import clasificacionEte
from apps.gestion.models            import SeisPerdidas
from apps.gestion.models            import CausasTm
from apps.gestion.models            import areas
from apps.estado_paros_deta3.models import paros_deta3
from .get_no_turno                  import get_no_turno
from datetime                       import datetime, time, timedelta

# Create your models here.

class estados(models.Model):

    turno2,fecha_turno = get_no_turno(datetime.now())

    maquina            = models.ForeignKey(maquina,null=True,blank=True,on_delete=models.CASCADE)
    turno              = models.FloatField(default=turno2)
    fecha              = models.DateTimeField(default=timezone.now,null=True)
    fecha_creacion     = models.DateTimeField(default=timezone.now)
    FechaTurno         = models.DateTimeField(default=fecha_turno)
    Modo               = models.CharField(max_length=60,null=True,blank=True)
    Execution          = models.CharField(max_length=60,null=True,blank=True)
    Alarma             = models.CharField(max_length=60,null=True,blank=True)
    CorteViruta        = models.BooleanField(null=True,blank=True)
    paros_deta3        = models.ForeignKey(paros_deta3,null=True,blank=True,on_delete=models.CASCADE)
    deltaTime          = models.FloatField(null=True)

class estados_inicial(models.Model):

    turno2,fecha_turno = get_no_turno(datetime.now())
    maquina            = models.ForeignKey(maquina,null=True,blank=True,on_delete=models.CASCADE)
    turno              = models.FloatField(default=turno2)
    fecha              = models.DateTimeField(default=timezone.now,null=True)
    fecha_creacion     = models.DateTimeField(default=timezone.now)
    FechaTurno         = models.DateTimeField(default=fecha_turno)
    Modo               = models.CharField(max_length=60,null=True,blank=True)
    Execution          = models.CharField(max_length=60,null=True,blank=True)
    Alarma             = models.CharField(max_length=60,null=True,blank=True)
    CorteViruta        = models.BooleanField(null=True,blank=True)
    paros_deta3        = models.ForeignKey(paros_deta3,null=True,blank=True,on_delete=models.CASCADE)
    deltaTime          = models.FloatField(null=True)
