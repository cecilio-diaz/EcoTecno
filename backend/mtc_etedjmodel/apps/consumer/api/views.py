from  django.shortcuts           import render
from rest_framework              import viewsets
from url_filter.integrations.drf import DjangoFilterBackend

from .serializers                import profile_Serializers
from apps.consumer.models        import profile

class profile_Set(viewsets.ModelViewSet):
    queryset         = profile.objects.all().order_by('-id')
    serializer_class = profile_Serializers
    filter_backends  = [DjangoFilterBackend,]
    filter_fields    = ['id','name','description']
