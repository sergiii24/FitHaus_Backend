from colections.models import Collection
from rest_framework import serializers


class colectionserializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class CollectionDTOSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        exclude = ('id')

    predef_routines = serializers.ListField(child=serializers.CharField())
