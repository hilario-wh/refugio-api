from django.conf.urls import url

from modulos.adopcion.views import index, solicitud_list, solicitud_view, solicitud_update, solicitud_delete, \
    SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
    url(r'^$', index),
    url(r'^class/solicitud/listar$', SolicitudList.as_view(), name='class_solicitud_listar'),
    url(r'^class/solicitud/nuevo$', SolicitudCreate.as_view(), name='class_solicitud_crear'),
    url(r'^class/solicitud/editar/(?P<pk>\d+)$', SolicitudUpdate.as_view(), name='class_solicitud_editar'),
    url(r'^class/solicitud/eliminar/(?P<pk>\d+)$', SolicitudDelete.as_view(), name='class_solicitud_eliminar'),

    url(r'^function/solicitud/listar$', solicitud_list, name='function_solicitud_listar'),
    url(r'^function/solicitud/nuevo', solicitud_view, name='function_solicitud_crear'),
    url(r'^function/solicitud/editar/(?P<solicitud_id>\d+)$', solicitud_update, name='function_solicitud_editar'),
    url(r'^function/solicitud/eliminar/(?P<solicitud_id>\d+)$', solicitud_delete, name='function_solicitud_eliminar'),

]
