from  django.shortcuts           import render
from rest_framework              import viewsets
from url_filter.integrations.drf import DjangoFilterBackend

from .serializers                import product_Serializers
from .serializers                import seller_product_Serializers
from apps.product.models        import product
from apps.product.models        import seller_product


class product_Set(viewsets.ModelViewSet):
    queryset         = product.objects.all().order_by('-id')
    serializer_class = product_Serializers
    filter_backends  = [DjangoFilterBackend,]
    filter_fields    = ['id','name','description']


class seller_product_Set(viewsets.ModelViewSet):
    queryset         = seller_product.objects.all().order_by('-id')
    serializer_class = seller_product_Serializers
    filter_backends  = [DjangoFilterBackend,]
    filter_fields    = ['id','seller','Products']
