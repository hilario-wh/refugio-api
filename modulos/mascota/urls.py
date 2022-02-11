from django.conf.urls import url

from modulos.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete,\
    MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

urlpatterns = [
    url(r'^$', index, name='index'),


    url(r'^class/nuevo$', MascotaCreate.as_view(), name='class_mascota_crear'),
    url(r'^class/listar$', MascotaList.as_view(), name='class_mascota_listar'),
    url(r'^class/editar/(?P<pk>\d+)/$', MascotaUpdate.as_view(), name='class_mascota_editar'),
    url(r'^class/eliminar/(?P<pk>\d+)/$', MascotaDelete.as_view(), name='class_mascota_eliminar'),

    url(r'^function/nuevo$', mascota_view, name='function_mascota_crear'),
    url(r'^function/listar$', mascota_list, name='function_mascota_listar'),
    url(r'^function/editar/(?P<id_mascota>\d+)/$', mascota_edit, name='function_mascota_editar'),
    url(r'^function/eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name='function_mascota_eliminar'),
]
