from objectives.models import Objective
from rest_framework import serializers


class ObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objective
        fields = '__all__'
