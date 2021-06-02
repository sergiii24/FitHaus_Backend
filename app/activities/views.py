from classes.models import Class
from exercises.models import Exercise
from exercises.serializers import ExerciseSerializer
from rest_framework import viewsets


class ActivitiesViewSet(viewsets.ModelViewSet):
    ExercisesQuery = Exercise.objects.all()
    ClassQuery = Class.objects.all()
    queryset = ExercisesQuery
    serializer_class = ExerciseSerializer
