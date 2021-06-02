from classes.models import Class
from classes.models import ClassDTO
from rest_framework import serializers


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class ClassNoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        exclude = ('pre', 'videoclass')


class ClassImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('pre', 'videoclass')


class ClassDTOSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDTO
        exclude = ('id',)

    categories = serializers.ListField(child=serializers.CharField())
