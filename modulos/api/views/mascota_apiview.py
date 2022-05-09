from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from modulos.mascota.models import Mascota
from modulos.api.serializers import MascotaSerializer, PersonaSerializer


class MascotaList(APIView):
    """
    APIView | List all pets or create a new one
    """
    def get(self, request):
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MascotaSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class MascotaDetails(APIView):
    """
    APIView | Retrieve, update or delete a pet
    """
    def get_object(self, pk):
        try:
            mascota = Mascota.objects.get(pk=pk)
            return mascota
        except Mascota.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        mascota = self.get_object(pk)
        serializer = MascotaSerializer(mascota)
        return Response(serializer.data)

    def put(self, request, pk):
        mascota = self.get_object(pk)
        serializer = MascotaSerializer(mascota, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        mascota = self.get_object(pk)
        mascota.delete()
        return Response(status=204)


class MascotaPersonaList(APIView):
    """
    APIView | List pet owner
    """
    def get_object(self, pk):
        try:
            mascota = Mascota.objects.get(pk=pk)
            return mascota
        except Mascota.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        mascota = self.get_object(pk)
        persona = mascota.persona
        if persona is not None:
            serializer = PersonaSerializer(persona)
            return Response(serializer.data)
        raise Http404