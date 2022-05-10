from rest_framework import authentication, generics, permissions


from modulos.api.serializers import VacunaSerializer
from modulos.mascota.models import Vacuna


class VacunaListGeneric(generics.ListAPIView):
    """
    Generic Views | List all people
    """
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = Vacuna.objects.all()
    serializer_class = VacunaSerializer