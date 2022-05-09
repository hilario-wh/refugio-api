from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.response import Response

from modulos.api.serializers import MascotaSerializer, PersonaSerializer
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


class MascotaPersonaListGeneric(generics.RetrieveAPIView):
    """
    Generic Views | List pet owner
    """

    def retrieve(self, request, *args, **kwargs):
        mascota = get_object_or_404(Mascota, pk=self.kwargs.get('pk'))
        persona = mascota.persona
        if persona is not None:
            serializer = PersonaSerializer(persona)
            return Response(serializer.data)
        raise Http404