from rest_framework import serializers
from modulos.adopcion.models import Persona
from modulos.mascota.models import Mascota, Vacuna


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = [
            'id',
            'nombre',
            'apellido',
            'edad',
            'telefono',
            'email',
            'domicilio',
        ]


class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = [
            'id',
            'nombre',
        ]

class MascotaSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer(read_only=True)
    vacuna = VacunaSerializer(read_only=True, many=True)
    class Meta:
        model = Mascota
        fields = [
            'id',
            #'image',
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]