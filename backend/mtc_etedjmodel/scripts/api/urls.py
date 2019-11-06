# APIs Configuration
from django.urls       import include, path
from .                 import views
from rest_framework    import routers




router = routers.DefaultRouter()
router.register('api/v1/estado_paros_enca', views.EmpresaSet)

urlpatterns = [
    path('',include(router.urls))

]
