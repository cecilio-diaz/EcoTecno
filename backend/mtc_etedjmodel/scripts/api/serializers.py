""" Maquinas EAM serializers """

# Danjo Rest Framework
from rest_framework import serializers
# Modelos
from apps.estado_paros_enca.models import Paros_enca

class Paros_encaSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Paros_enca
        fields = (
            'id',
            'nombre',
            'ID_paros_enca',
                  )
