from rest_framework import serializers
from classes.models import Classes
from classes.models import ClassesDTO


class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'

class ClassesNoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        exclude = ('pre', 'videoclass')


class ClassesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ('pre', 'videoclass')

class ClassesDTOSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassesDTO
        exclude = ('id',)
    categories = serializers.ListField(child=serializers.CharField())