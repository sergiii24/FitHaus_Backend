from rest_framework import serializers
from exercises.models import Exercise
from categories.serializers import CategorySerializer


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class ExerciseNoImageSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    POSIBLE_TYPE = [
        ('E', 'Exercise'),
        ('C', 'Class')
    ]
    type = serializers.ChoiceField(choices=POSIBLE_TYPE)
    description = serializers.CharField(max_length=200)
    POSIBLE_AGE = [
        ('K', 'Kid'),
        ('T', 'Teenager'),
        ('A', 'Adult'),
        ('E', 'Elder')
    ]
    age = serializers.ChoiceField(choices=POSIBLE_AGE)
    POSIBLE_DIFFICULTY = [
        ('E', 'Easy'),
        ('M', 'Medium'),
        ('H', 'Hard')
    ]
    difficulty = serializers.ChoiceField(choices=POSIBLE_DIFFICULTY)
    length = serializers.IntegerField()
    categories = CategorySerializer(read_only=True, many=True)
    POSIBLE_MUSCLE = [
        ('Bi', 'Biceps'),
        ('Tr', 'Triceps'),
        ('Fa', 'Forearm'),
        ('Ch', 'Chest'),
        ('Sh', 'Shoulder'),
        ('Do', 'Dorsal'),
        ('Gl', 'Gluteus'),
        ('Fe', 'Femoral'),
        ('Qu', 'Quadriceps'),
        ('Ca', 'Calf'),
        ('Co', 'Core')
    ]
    muscle = serializers.ChoiceField(choices=POSIBLE_MUSCLE)


class ExerciseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('pre', 'muscleimage', 'videotutorial', 'videoexercise')