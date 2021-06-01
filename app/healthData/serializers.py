from rest_framework import serializers
from healthData.models import HealthData, HealthDataDTO


class HealthDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthData
        fields = '__all__'


class HealthDataDTOSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthDataDTO
        fields = '__all__'