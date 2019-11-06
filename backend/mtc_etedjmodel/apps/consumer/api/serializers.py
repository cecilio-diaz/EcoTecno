""" Maquinas EAM serializers """
# Modelos
# Danjo Rest Framework
from rest_framework          import serializers
from apps.consumer.models    import profile

class profile_Serializers(serializers.ModelSerializer):
    class Meta:
        model  = profile
        fields = (
                'id',
                'name',
                'description',
                'image',
        )
