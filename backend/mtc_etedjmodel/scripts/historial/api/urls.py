# APIs Configuration
from django.urls       import include, path
from .                 import views
from rest_framework    import routers



router = routers.DefaultRouter()
router.register('api/v1/historial/', views.estado_Set)
router.register('api/v1/historial_inicial/', views.estado_inicial_Set)

urlpatterns = [
    path('',include(router.urls))
              ]
