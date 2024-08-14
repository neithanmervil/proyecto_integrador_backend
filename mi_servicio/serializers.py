from rest_framework import serializers
from .models import Dispositivo, Prestamo

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = '__all__'

class PrestamoSerializer(serializers.ModelSerializer):
    dispositivo = serializers.PrimaryKeyRelatedField(queryset=Dispositivo.objects.all(), required=True)

    class Meta:
        model = Prestamo
        fields = '__all__'

    def create(self, validated_data):
        dispositivo = validated_data.pop('dispositivo', None)
        prestamo = Prestamo.objects.create(**validated_data, dispositivo=dispositivo)
        return prestamo
