from django.db import models
# Create your models here.
from django.utils import timezone
# Create your models here.

class service(models.Model):

    date_create        = models.DateTimeField(default=timezone.now)
    date_update        = models.DateTimeField(auto_now=True)
    country            = models.CharField(default='italy',null=True,max_length=60)
    city               = models.CharField(default='milano',null=True,max_length=60)
    dataSource         = models.CharField(default='',null=True,blank=True,max_length=60)
    latitude           = models.FloatField(default=45.515904,null=True)
    longitude          = models.FloatField(default=9.210390,null=True)
    status             = models.BooleanField(default=True,null=True,blank=True)
    IoTdevice          = models.CharField(default='italy',null=True,max_length=60)
    value              = models.IntegerField(default=0,null=True)
    unit               = models.CharField(default='°C',null=True,max_length=60)
