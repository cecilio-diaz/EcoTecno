from django.contrib import admin
from .models        import service
# Register your models here.


admin.site.site_header = 'SMART POWER CHARGE'

class Adminservice(admin.ModelAdmin):

    list_display = ('date_create',
                    'date_update',
                    'country',
                    'city',
                    'dataSource',
                    'latitude',
                    'longitude',
                    'status',
                    'placesAvailable',
                    'placesOccupied',
                    'radius',
                    )
    search_fields = (
            'country',
            'city',
            'dataSource',
            'status',
             )

    list_filter = (
            'country',
            'city',
            'dataSource',
            'status',
            )
admin.site.register(service,Adminservice)
