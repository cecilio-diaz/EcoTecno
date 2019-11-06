from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models        import product
from .models        import seller_product
# Register your models here.



class Adminproduct(admin.ModelAdmin):
    list_display = ('product',
                    'description',
                    'image',
                    )

admin.site.register(product,Adminproduct)

class Adminseller_seller_product(admin.ModelAdmin):

    pass

admin.site.register(seller_product,Adminseller_seller_product)
