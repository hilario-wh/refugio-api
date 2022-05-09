# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render

from rest_framework import authentication, permissions, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from modulos.api.serializers import MascotaSerializer, PersonaSerializer
from modulos.mascota.models import Mascota


@api_view(['GET', 'POST'])
@authentication_classes([authentication.SessionAuthentication])
@permission_classes([permissions.IsAdminUser])
def mascota_list(request):
    """
    DECORATOR | List all pets, or create a new one.
    """
    if request.method == 'GET':
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = MascotaSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([authentication.SessionAuthentication])
@permission_classes([permissions.IsAdminUser])
def mascota_detail(request, pk):
    """
    DECORATOR | Retrieve, update or delete a pet
    """
    try:
        mascota = Mascota.objects.get(pk=pk)
    except Mascota.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        serializer = MascotaSerializer(mascota)
        return Response(serializer.data)

    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = MascotaSerializer(mascota, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        mascota.delete()
        return Response(status=204)


@api_view(['GET'])
@authentication_classes([authentication.SessionAuthentication])
@permission_classes([permissions.IsAdminUser])
def mascota_persona_list(request, pk):
    """
    DECORATOR | List pet owner
    """

    try:
        mascota = Mascota.objects.get(pk=pk)
    except Mascota.DoesNotExist:
        raise Http404
        
    if request.method == 'GET':
        persona = mascota.persona
        if persona is not None:
            serializer = PersonaSerializer(persona)
            return Response(serializer.data)
        raise Http404
