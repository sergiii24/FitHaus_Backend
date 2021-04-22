from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from exercises.models import Exercise
from exercises.serializers import ExerciseSerializer


class ExercisesViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['muscle']
