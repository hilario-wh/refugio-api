from email.mime import base
from django.conf.urls import url

from modulos.api.views.mascota_decorator import mascota_list, mascota_detail, mascota_persona_list
from modulos.api.views.mascota_apiview import MascotaDetails, MascotaList, MascotaPersonaList
from modulos.api.views.mascota_viewset import MascotaViewset
from modulos.api.views.mascotas_generic import MascotaDetailsGeneric, MascotaListGeneric, MascotaPersonaListGeneric
from modulos.api.views.mascota_front import (
    front_mascota_create,
    front_mascota_delete,
    front_mascota_edit,
    front_mascota_list,
    front_mascota_persona_details,
)
from modulos.api.views.persona_generic import PersonaListGeneric
from modulos.api.views.vacuna_generic import VacunaListGeneric
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # Decorator
    url(r'^v1/mascotas$', mascota_list, name='mascota_list_v1'),
    url(r'^v1/mascotas/(?P<pk>\d+)$', mascota_detail, name='mascota_details_v1'),
    url(r'^v1/mascotas/(?P<pk>\d+)/persona$', mascota_persona_list, name='mascota_persona_list_v1'),
    # APIView
    url(r'^v2/mascotas$', MascotaList.as_view(), name='mascota_list_v2'),
    url(r'^v2/mascotas/(?P<pk>\d+)$', MascotaDetails.as_view(), name='mascota_details_v2'),
    url(r'^v2/mascotas/(?P<pk>\d+)/persona$', MascotaPersonaList.as_view(), name='mascota_persona_list_v2'),
    # Generic
    url(r'^v3/mascotas$', MascotaListGeneric.as_view(), name='mascota_list_v3'),
    url(r'^v3/mascotas/(?P<pk>\d+)$', MascotaDetailsGeneric.as_view(), name='mascota_details_v3'),
    url(r'^v3/mascotas/(?P<pk>\d+)/persona$', MascotaPersonaListGeneric.as_view(), name='mascota_persona_list_v3'),
    url(r'^v3/personas$', PersonaListGeneric.as_view(), name='persona_list'),
    url(r'^v3/vacunas$', VacunaListGeneric.as_view(), name='vacuna_list'),
    # Viewset
    url(r'^v4/mascotas$', MascotaViewset.as_view({'get':'list', 'post':'create'}), name='mascota_list_v4'),
    url(r'^v4/mascotas/(?P<pk>\d+)$', MascotaViewset.as_view({'get':'retrieve', 'put':'update', 'delete': 'destroy'}), name='mascota_details_v4'),
    url(r'^v4/mascotas/(?P<pk>\d+)/persona$', MascotaViewset.as_view({'get':'persona'}), name='mascota_persona_list_v4'),

    # Ejemplo Consumo
    url(r'^nuevo$', front_mascota_create, name='api_mascota_crear'),
    url(r'^listar$', front_mascota_list, name='api_mascota_listar'),
    url(r'^editar/(?P<pk>\d+)/$', front_mascota_edit, name='api_mascota_editar'),
    url(r'^mascota/(?P<pk>\d+)/persona$', front_mascota_persona_details, name='api_mascota_persona_details'),
    url(r'^eliminar/(?P<pk>\d+)/$', front_mascota_delete, name='api_mascota_eliminar'),
]

#router = DefaultRouter()
#router.register(r'^v4/mascotas', MascotaViewset, base_name='mascota_v4')
#urlpatterns += router.urls