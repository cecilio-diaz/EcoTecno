from django.db import models
from apps.seller.models import profile
# Create your models here.


class  product(models.Model):

    product            = models.CharField(default='Pomodoro',null=True,max_length=60,blank=True)
    description        = models.CharField(default='description',null=True,max_length=250)
    image              = models.CharField(default='description',null=True,max_length=250)


class  seller_product(models.Model):
    product        = models.ForeignKey(product,null=True,blank=True,on_delete=models.CASCADE)
    sellers        = models.ManyToManyField(profile)
