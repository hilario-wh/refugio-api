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

    def to_representation(self, instance):
        values = super(MascotaSerializer, self).to_representation(instance)
        if values['persona'] is not None: values['persona'] = PersonaSerializer(instance.persona).data
        values['vacuna'] = VacunaSerializer(instance.vacuna, many=True).data
        return values
        