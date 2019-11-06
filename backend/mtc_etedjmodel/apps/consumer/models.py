from django.db import models

# Create your models here.
from django.utils import timezone
# Create your models here.

class  profile(models.Model):

    date_update        = models.DateTimeField(auto_now=True)
    name               = models.CharField(default='italy',null=True,max_length=60)
    description        = models.CharField(default='description',null=True,max_length=250)
    image              = models.FileField(null=False,blank=False,unique=True, upload_to= "scripts/")
