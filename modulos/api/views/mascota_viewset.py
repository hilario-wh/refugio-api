from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from yaml import serialize

from modulos.api.serializers import MascotaSerializer
from modulos.mascota.models import Mascota


class MascotaViewset(viewsets.ViewSet):
    """
    ViewSet | Full CRUD class
    """
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