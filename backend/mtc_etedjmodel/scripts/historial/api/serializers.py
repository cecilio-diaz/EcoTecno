""" Maquinas EAM serializers """
# Danjo Rest Framework
from rest_framework import serializers
# Modelos
from apps.historial.models import estados
from apps.historial.models import estados_inicial

class estados_Serializers(serializers.ModelSerializer):
    class Meta:
        model  = estados
        fields = (
            'id',
            'maquina',
            'Modo',
            'Execution',
            'Alarma',
            'CorteViruta',
            'paros_deta3',
            'deltaTime',
            'fecha',
           )

class estados_inicial_Serializers(serializers.ModelSerializer):
    class Meta:
        model  = estados_inicial
        fields = (
            'id',
            'maquina',
            'Modo',
            'Execution',
            'Alarma',
            'CorteViruta',
            'paros_deta3',
            'deltaTime',
            'fecha',
           )
