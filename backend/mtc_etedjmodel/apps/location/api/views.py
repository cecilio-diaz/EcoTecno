from  django.shortcuts           import render
from rest_framework              import viewsets
from url_filter.integrations.drf import DjangoFilterBackend

from .serializers                import localization_Serializers
from apps.location.models     import service

class localization_Set(viewsets.ModelViewSet):
    queryset         = service.objects.all().order_by('-id')
    serializer_class = localization_Serializers
    filter_backends  = [DjangoFilterBackend,]
    filter_fields    = ['date_create','country','city','status','placesAvailable','seller']
