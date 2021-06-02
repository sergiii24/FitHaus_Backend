from exercises.models import Exercise
from exercises.models import ExerciseDTO
from exercises.serializers import ExerciseDTOSerializer
from exercises.serializers import ExerciseNoImageSerializer
from exercises.serializers import ExerciseSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
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

    def create(self, request):
        try:
            data = JSONParser().parse(request)
            ex_serializer = ExerciseNoImageSerializer(data=data)
            # data = request.FILES['pre']
            # ex_image_serializer = ExerciseNoImageSerializer(data=data)
            if ex_serializer.is_valid():
                ex = Exercise()
                ex.type = ex_serializer.validated_data.get('type')
                ex.name = ex_serializer.validated_data.get('name')
                ex.description = ex_serializer.validated_data.get('description')
                ex.age = ex_serializer.validated_data.get('age')
                ex.difficulty = ex_serializer.validated_data.get('difficulty')
                ex.length = ex_serializer.validated_data.get('length')
                ex.save()
                categories = []
                cat = ex_serializer.validated_data.get('categories')
                for c in cat:
                    categories.append(c.category)
                ex.categories.set(categories)
                ex.pre = ex_image_serializer.validated_data.get('pre')
                ex.muscleimage = ex_image_serializer.validated_data.get('muscleimage')
                ex.videotutorial = ex_image_serializer.validated_data.get('videotutorial')
                ex.videoexercise = ex_image_serializer.validated_data.get('videoexercise')
                ex.muscle = ex_serializer.validated_data.get('muscle')
                ex.save()
                return Response(ex_serializer.data, status=status.HTTP_201_CREATED)
            return Response(ex_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exercise.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        try:
            exercise = Exercise.objects.get(name=pk)
            categories = []
            cat = exercise.categories.all()
            for c in cat:
                categories.append(c.category)
            dto = ExerciseDTO(type=exercise.type,
                              name=exercise.name,
                              description=exercise.description,
                              age=exercise.age,
                              difficulty=exercise.difficulty,
                              length=exercise.length,
                              pre=exercise.pre,
                              muscleimage=exercise.muscleimage,
                              videotutorial=exercise.videotutorial,
                              videoexercise=exercise.videoexercise,
                              muscle=exercise.muscle)
            dto.categories = categories
            serializer = ExerciseDTOSerializer(dto)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exercise.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk):
        try:
            data = JSONParser().parse(request)
            exercise = Exercise.objects.get(name=pk)
            serializer = ExerciseSerializer(exercise, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exercise.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        try:
            exercise = Exercise.objects.get(name=pk)
            serializer = ExerciseSerializer(exercise)
            exercise.delete()
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exercise.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
