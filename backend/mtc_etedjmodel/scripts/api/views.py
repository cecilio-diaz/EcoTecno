from  django.shortcuts             import render
from rest_framework                import viewsets
from .serializers                  import Paros_encaSerializers
from apps.estado_paros_enca.models import Paros_enca
from url_filter.integrations.drf   import DjangoFilterBackend

class Paros_encaSet(viewsets.ModelViewSet):

    queryset         = Paros_enca.objects.all().order_by('-id')
    serializer_class = Paros_encaSerializers
    filter_backends = [DjangoFilterBackend,]
    filter_fields    = ['nombre',]
