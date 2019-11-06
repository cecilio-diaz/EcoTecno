from django.contrib import admin
# Register your models here.
from django.db              import models
from apps.historial.models  import estados
from apps.historial.models  import estados_inicial
from django.utils           import timezone
# Create your models here.

class estadoAdmin(admin.ModelAdmin):

    list_display = ('pk','maquina','turno','Modo','Execution','Alarma','CorteViruta','paros_deta3','deltaTime')

    search_fields = (
            'maquina',
            'turno',
            'Modo',
            'Execution',
            'Alarma',
             )

    list_filter = (
            'maquina',
            'paros_deta3',
            'turno',
            'Modo',
            'Execution',
            'Alarma',
            )

admin.site.register(estados,estadoAdmin)

class estado_inicialAdmin(admin.ModelAdmin):
    list_display = ('pk','maquina','turno','Modo','Execution','Alarma','CorteViruta','paros_deta3','deltaTime')

    search_fields = (
            'maquina',
            'turno',
            'Modo',
            'Execution',
            'Alarma',
             )
    list_filter = (
            'maquina',
            'paros_deta3',
            'turno',
            'Modo',
            'Execution',
            'Alarma',
            )

admin.site.register(estados_inicial,estado_inicialAdmin)
