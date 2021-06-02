from rest_framework import serializers
from colections.models import Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

class CollectionDTOSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        exclude = ('id')
    predef_routines = serializers.ListField(child=serializers.CharField())
