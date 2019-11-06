from django.db import models
# Create your models here.
from django.utils import timezone
from apps.seller.models import profile
# Create your models here.

class service(models.Model):
    seller             = models.ForeignKey(profile,null=True,blank=True,on_delete=models.CASCADE)
    date_create        = models.DateTimeField(default=timezone.now)
    date_update        = models.DateTimeField(auto_now=True)
    country            = models.CharField(default='italy',null=True,max_length=60,blank=True)
    city               = models.CharField(default='milano',null=True,max_length=60,blank=True)
    dataSource         = models.CharField(default='',null=True,blank=True,max_length=60)
    status             = models.BooleanField(default=True,null=True,blank=True)
    IoTdevice          = models.CharField(default='WioLink',null=True,max_length=60)
    SensorType         = models.CharField(default='temperture',null=True,max_length=60)
    value              = models.IntegerField(default=0,null=True)
    unit               = models.CharField(default='°C',null=True,max_length=60)
