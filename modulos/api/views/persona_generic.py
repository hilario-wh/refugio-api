from rest_framework import authentication, generics, permissions

from modulos.adopcion.models import Persona
from modulos.api.serializers import PersonaSerializer


class PersonaListGeneric(generics.ListAPIView):
    """
    Generic Views | List all people
    """
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer