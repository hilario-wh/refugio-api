from email.mime import base
from django.conf.urls import url

from modulos.api.views.mascota_decorator import mascota_list, mascota_detail
from modulos.api.views.mascota_apiview import MascotaDetails, MascotaList
from modulos.api.views.mascota_viewset import MascotaViewset
from modulos.api.views.mascotas_generic import MascotaDetailsGeneric, MascotaListGeneric
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # Decorator
    url(r'^v1/mascotas$', mascota_list, name='mascota_list_v1'),
    url(r'^v1/mascotas/(?P<pk>\d+)$', mascota_detail, name='mascota_details_v1'),
    # APIView
    url(r'^v2/mascotas$', MascotaList.as_view(), name='mascota_list_v2'),
    url(r'^v2/mascotas/(?P<pk>\d+)$', MascotaDetails.as_view(), name='mascota_details_v2'),
    # Generic
    url(r'^v3/mascotas$', MascotaListGeneric.as_view(), name='mascota_list_v3'),
    url(r'^v3/mascotas/(?P<pk>\d+)$', MascotaDetailsGeneric.as_view(), name='mascota_details_v3'),
]

router = DefaultRouter()
router.register(r'^v4/mascotas', MascotaViewset, base_name='mascota_v4')
urlpatterns += router.urls