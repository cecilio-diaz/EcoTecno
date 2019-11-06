""" Maquinas EAM serializers """
# Modelos
# Danjo Rest Framework
from rest_framework        import serializers
from apps.product.models  import product
from apps.product.models  import seller_product


class product_Serializers(serializers.ModelSerializer):
    class Meta:
        model  = product
        fields = (
                'id',
                'product',
                'description',
                'image',
        )

class seller_product_Serializers(serializers.ModelSerializer):
    class Meta:
        model  = seller_product
        fields = (
                'id',
                'sellers',
                'product',
        )
