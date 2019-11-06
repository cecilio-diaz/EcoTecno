from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models        import profile
# Register your models here.


admin.site.site_header = 'BlaBlaFarm'

class Adminprofile(admin.ModelAdmin):

    list_display = ('date_update',
                    'name',
                    'description',
                    'latitude',
                    'longitude',
                    'image',
                    'verified',
                    'rating')

    search_fields = ('name',
                     'rating',
                     )

    list_filter = (
            'name',
            'rating',
            )
