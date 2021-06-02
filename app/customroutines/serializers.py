from customroutines.models import CustomRoutine
from rest_framework import serializers


class CustomRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomRoutine
        fields = '__all__'
