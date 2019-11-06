""" Maquinas EAM serializers """
# Modelos
# Danjo Rest Framework
from rest_framework              import serializers
from apps.location.models        import service

class localization_Serializers(serializers.ModelSerializer):
    class Meta:
        model  = service
        fields = (
                'id',
                'seller',
                'date_create',
                'country',
                'city',
                'dataSource',
                'status',
                'IoTdevice',
                'SensorType',
                'value',
                'unit')
