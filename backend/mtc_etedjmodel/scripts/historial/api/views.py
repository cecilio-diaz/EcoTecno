from  django.shortcuts              import render
from rest_framework                 import viewsets
from .serializers                   import estados_Serializers
from .serializers                   import estados_inicial_Serializers
from .serializers                   import estados_Serializers
from apps.historial.models          import estados
from apps.historial.models          import estados_inicial
from url_filter.integrations.drf    import DjangoFilterBackend


class estado_Set(viewsets.ModelViewSet):

    queryset         = estados.objects.all().order_by('-id')
    serializer_class = estados_Serializers
    filter_backends  = [DjangoFilterBackend,]
    filter_fields    = ['maquina',]

class estado_inicial_Set(viewsets.ModelViewSet):

    queryset         = estados_inicial.objects.all().order_by('-id')
    serializer_class = estados_inicial_Serializers
    filter_backends  = [DjangoFilterBackend,]
    filter_fields    = ['maquina',]
