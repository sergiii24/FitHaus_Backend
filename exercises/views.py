from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from exercises.models import Exercise
from exercises.serializers import ExerciseSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class ExercisesViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'type', 'age', 'difficulty', 'muscle', 'categories']
