from rest_framework import serializers
from programs.models import Program
from programs.models import ProgramDTO

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class ProgramDTOSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramDTO
        exclude = ('id')
    predef_routines = serializers.ListField(child=serializers.CharField())