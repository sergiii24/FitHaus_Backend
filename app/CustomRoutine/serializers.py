from rest_framework import serializers
from CustomRoutine.models import CustomRoutine


class CustomRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomRoutine
        fields = '__all__'

