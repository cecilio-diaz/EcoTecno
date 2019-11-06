# Register your models here.

from django.contrib import admin
from .models        import profile
# Register your models here.


admin.site.site_header = 'BlaBlaFarm'

class Adminprofile(admin.ModelAdmin):

    list_display = ('date_update',
                    'name',
                    'description',
                    'image',)

    search_fields = ('name',
                     'description',
                     )

    list_filter = (
            'name',
            'description',
            )

admin.site.register(profile,Adminprofile)
