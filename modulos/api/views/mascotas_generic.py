from rest_framework import generics

from modulos.api.serializers import MascotaSerializer
from modulos.mascota.models import Mascota


class MascotaListGeneric(generics.ListCreateAPIView):
    """
    Generic Views | List all pets or create a new one
    """
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer


class MascotaDetailsGeneric(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic Views | Retrieve, update or delete a pet
    """
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer