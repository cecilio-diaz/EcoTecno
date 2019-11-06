# APIs Configuration
from django.urls       import include, path
from .                 import views
from rest_framework    import routers


router = routers.DefaultRouter()
router.register('api/v1/product',       views.product_Set)
router.register('api/v1/seller_product', views.seller_product_Set)


urlpatterns = [
    path('',include(router.urls))
              ]
