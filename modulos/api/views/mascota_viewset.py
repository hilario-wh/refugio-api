from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import authentication, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from modulos.api.serializers import MascotaSerializer, PersonaSerializer
from modulos.mascota.models import Mascota


class MascotaViewset(viewsets.ViewSet):
    """
    ViewSet | Full CRUD class
    """
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def list(self, request):
        queryset = Mascota.objects.all()
        serializer = MascotaSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MascotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        mascota = get_object_or_404(Mascota, pk=pk)
        serializer = MascotaSerializer(mascota)
        return Response(serializer.data)

    def update(self, request, pk=None):
        mascota = get_object_or_404(Mascota, pk=pk)
        serializer = MascotaSerializer(mascota, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        mascota = get_object_or_404(Mascota, pk=pk)
        mascota.delete()
        return Response(status=204)

    @action(detail=True, methods=['get'])
    def persona(self, request, pk=None):
        """
        ViewSet | Get pet owner
        """
        mascota = get_object_or_404(Mascota, pk=pk)
        persona = mascota.persona
        if persona is not None:
            serializer = PersonaSerializer(persona)
            return Response(serializer.data)
        raise Http404
