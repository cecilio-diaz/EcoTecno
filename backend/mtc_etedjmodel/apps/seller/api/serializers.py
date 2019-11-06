""" Maquinas EAM serializers """
# Modelos
# Danjo Rest Framework
from rest_framework              import serializers
from apps.seller.models          import profile

class profile_Serializers(serializers.ModelSerializer):
    class Meta:
        model  = profile
        fields = (
                'id',
                'profile',
                'description',
                'latitude',
                'longitude',
                'image',
                'verified',
                'rating',
        )
