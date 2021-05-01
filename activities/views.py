from rest_framework import viewsets
from exercises.models import Exercise
from classes.models import Classes
from exercises.serializers import ExerciseSerializer


class ActivitiesViewSet(viewsets.ModelViewSet):
    ExercisesQuery = Exercise.objects.all()
    ClassesQuery = Classes.objects.all()
    queryset = ExercisesQuery
    serializer_class = ExerciseSerializer

