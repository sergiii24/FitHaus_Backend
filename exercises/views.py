from rest_framework import viewsets
from exercises.models import Exercise
from exercises.serializers import ExerciseSerializer


class ExercisesViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
