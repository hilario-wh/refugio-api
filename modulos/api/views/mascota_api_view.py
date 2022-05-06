# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render
from modulos.api.serializers import MascotaSerializer

from modulos.mascota.models import Mascota


@api_view(['GET', 'POST'])
def mascota_list(request):
    """
    List all pets, or create a new one.
    """
    if request.method == 'GET':
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)
