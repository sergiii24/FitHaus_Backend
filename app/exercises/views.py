from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from exercises.models import Exercise
from exercises.serializers import ExerciseSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response


class ExercisesViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Exercise.objects.all()
        name = request.query_params.get('name')
        type = request.query_params.get('type')
        age = request.query_params.get('age')
        difficulty = request.query_params.get('difficulty')
        muscle = request.query_params.get('muscle')
        categories = request.query_params.get('categories')
        if name is not None:
            queryset = queryset.filter(name=name)
        elif type is not None:
            queryset = queryset.filter(type=type)
        elif age is not None:
            queryset = queryset.filter(age=age)
        elif difficulty is not None:
            queryset = queryset.filter(difficulty=difficulty)
        elif muscle is not None:
            queryset = queryset.filter(muscle=muscle)
        elif categories is not None:
            queryset = queryset.filter(categories=categories)
        serializer = ExerciseSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #def create(self, request):
