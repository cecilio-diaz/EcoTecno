from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models        import profile
# Register your models here.


class AdminProfile(admin.ModelAdmin):

    list_display = ('date_update',
                    'profile',
                    'description',
                    'latitude',
                    'longitude',
                    'image',
                    'verified',
                    'rating',
                    )

    search_fields = ('profile',
                     'rating',
                     )

    list_filter = (
            'profile',
            'rating',
            )
admin.site.register(profile,AdminProfile)
