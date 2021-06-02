from predefinedroutines.models import PredefinedRoutine
from rest_framework import serializers


class PredfinedRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredefinedRoutine
        exclude = ['image',]
