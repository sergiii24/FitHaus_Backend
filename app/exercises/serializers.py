from rest_framework import serializers
from exercises.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class ExerciseNoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        exclude = ('pre', 'muscleimage', 'videotutorial', 'videoexercise')

class ExerciseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('pre', 'muscleimage', 'videotutorial', 'videoexercise')