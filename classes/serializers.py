from rest_framework import serializers
from classes.models import Classes


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'

