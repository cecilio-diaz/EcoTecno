from django.contrib                    import admin
from django.urls                       import path
from django.conf                       import settings
from django.conf.urls                  import url, include
from django.views.static               import serve
from .views                            import hello_world
from .views                            import insert_buffer_data
from django.urls                       import include, path
from rest_framework                    import routers

from apps.location.api.views       import  localization_Set


from rest_framework.urlpatterns import format_suffix_patterns


# APIs Configuration


router = routers.DefaultRouter()

router.register('api/v1/services',localization_Set)
#router.register('api/v1/maquina_mtc'        ,MaquinaSet)

urlpatterns = [
    url('admin/', admin.site.urls),
    path('scanner/<str:maquina>/<str:causaTM>/',insert_buffer_data),
    path('',include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += [
             url(r'^media(?P<path>.*)$',serve,{
                    'document_root':settings.MEDIA_ROOT,
                    }),
            ]
