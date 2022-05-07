from django.conf.urls import url

from modulos.api.views.mascota_decorator import mascota_list, mascota_detail
from modulos.api.views.mascota_apiview import MascotaDetails, MascotaList

urlpatterns = [
    # Decorator
    url(r'^v1/mascotas$', mascota_list, name='mascota_list_v1'),
    url(r'^v1/mascotas/(?P<pk>\d+)$', mascota_detail, name='mascota_list_v1'),
    # APIView
    url(r'^v2/mascotas$', MascotaList.as_view(), name='mascota_list_v2'),
    url(r'^v2/mascotas/(?P<pk>\d+)$', MascotaDetails.as_view(), name='mascota_list_v2'),
]
