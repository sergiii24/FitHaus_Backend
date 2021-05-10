from django.core.exceptions import ValidationError
from rest_framework import serializers
from trainings.models import Training


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'


