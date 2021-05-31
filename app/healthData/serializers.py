from rest_framework import serializers
from healthData.models import HealthData


class HealthDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthData
        fields = '__all__'
