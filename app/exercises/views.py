from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from exercises.models import Exercise
from exercises.serializers import ExerciseSerializer, ExerciseNoImageSerializer, ExerciseImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.utils import json



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

    def create(self, request):
        try:
            data = json.loads(request.data['data'])
            ex_serializer = ExerciseNoImageSerializer(data=data)
            data = request.FILES
            ex_image_serializer = ExerciseNoImageSerializer(data=data)
            if ex_serializer.is_valid():
                ex = Exercise()
                ex.type = ex_serializer.validated_data.get('type')
                ex.name = ex_serializer.validated_data.get('name')
                ex.description = ex_serializer.validated_data.get('description')
                ex.age = ex_serializer.validated_data.get('age')
                ex.difficulty = ex_serializer.validated_data.get('difficulty')
                ex.length = ex_serializer.validated_data.get('length')
                ex.categories = ex_serializer.validated_data.get('categories')
                ex.pre = ex_image_serializer.validated_data.get('pre')
                ex.muscleimage = ex_image_serializer.validated_data.get('muscleimage')
                ex.videotutorial = ex_image_serializer.validated_data.get('videotutorial')
                ex.videoexercise = ex_image_serializer.validated_data.get('videoexercise')
                ex.muscle = ex_serializer.validated_data.get('muscle')
                ex.save()
                return Response(ex_serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exercise.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)