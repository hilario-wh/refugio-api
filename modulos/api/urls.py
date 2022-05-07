from django.conf.urls import url

from modulos.api.views.mascota_api_view import mascota_list, mascota_detail

urlpatterns = [

    url(r'^v1/mascotas$', mascota_list, name='mascota_list_v1'),
    url(r'^v1/mascotas/(?P<pk>\d+)$', mascota_detail, name='mascota_list_v1'),
]
