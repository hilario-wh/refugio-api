from django.conf.urls import url

from modulos.api.views.mascota_api_view import mascota_list

urlpatterns = [

    url(r'^v1/mascota$', mascota_list, name='mascota_list_v1'),
]
