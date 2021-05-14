from rest_framework import serializers
from PredefinedRoutine.models import PredefinedRoutine


class PredfinedRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredefinedRoutine
        fields = '__all__'

