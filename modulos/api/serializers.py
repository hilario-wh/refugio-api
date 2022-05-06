from rest_framework import serializers
from modulos.mascota.models import Mascota


class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = [
            'id',
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]