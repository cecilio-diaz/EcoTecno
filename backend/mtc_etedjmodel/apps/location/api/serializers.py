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
                'date_create',
                'country',
                'city',
                'dataSource',
                'latitude',
                'longitude',
                'status',
                'placesAvailable',
                'placesOccupied',
                'radius')
