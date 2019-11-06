from django.db import models

# Create your models here.


class  profile(models.Model):

    date_update        = models.DateTimeField(auto_now=True)
    name               = models.CharField(default='italy',null=True,max_length=60)
    description        = models.CharField(default='description',null=True,max_length=250)
    latitude           = models.FloatField(default=45.515904,null=True)
    longitude          = models.FloatField(default=9.210390,null=True)
    image              = models.FileField(null=False,blank=False,unique=True, upload_to= "scripts/")
    verified           = models.BooleanField(default=False,null=True,blank=True)
    rating             = models.FloatField(default=4,null=True)
