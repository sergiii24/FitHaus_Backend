from classes.models import Class
from classes.models import ClassDTO
from classes.serializers import ClassDTOSerializer
from classes.serializers import ClassNoImageSerializer
from classes.serializers import ClassSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


class ClassViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Class.objects.all()
        name = request.query_params.get('name')
        type = request.query_params.get('type')
        age = request.query_params.get('age')
        difficulty = request.query_params.get('difficulty')
        workarea = request.query_params.get('muscle')
        categories = request.query_params.get('categories')
        if name is not None:
            queryset = queryset.filter(name=name)
        elif type is not None:
            queryset = queryset.filter(type=type)
        elif age is not None:
            queryset = queryset.filter(age=age)
        elif difficulty is not None:
            queryset = queryset.filter(difficulty=difficulty)
        elif workarea is not None:
            queryset = queryset.filter(workearea=workarea)
        elif categories is not None:
            queryset = queryset.filter(categories=categories)
        if queryset.count() > 0:
            serializer = ClassSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        try:
            data = JSONParser().parse(request)
            class_serializer = ClassNoImageSerializer(data=data)
            # data = request.FILES['pre']
            # ex_image_serializer = ExerciseNoImageSerializer(data=data)
            if class_serializer.is_valid():
                cl = Class()
                cl.type = class_serializer.validated_data.get('type')
                cl.name = class_serializer.validated_data.get('name')
                cl.description = class_serializer.validated_data.get('description')
                cl.age = class_serializer.validated_data.get('age')
                cl.difficulty = class_serializer.validated_data.get('difficulty')
                cl.length = class_serializer.validated_data.get('length')
                cl.trainer = class_serializer.validated_data.get('trainer')
                cl.save()
                categories = []
                cat = class_serializer.validated_data.get('categories')
                for c in cat:
                    categories.append(c.category)
                cl.categories.set(categories)
                # ex.videoclass = class_serializer.validated_data.get('videoclass')
                cl.workarea = class_serializer.validated_data.get('workarea')
                cl.save()
                return Response(class_serializer.data, status=status.HTTP_201_CREATED)
            return Response(class_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Class.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        try:
            cl = Class.objects.get(name=pk)
            categories = []
            cat = cl.categories.all()
            for c in cat:
                categories.append(c.category)
            dto = ClassDTO(type=cl.type,
                           name=cl.name,
                           description=cl.description,
                           age=cl.age,
                           difficulty=cl.difficulty,
                           length=cl.length,
                           trainer=cl.trainer,
                           pre=cl.pre,
                           videoclass=cl.videoclass)
            dto.categories = categories
            serializer = ClassDTOSerializer(dto)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Class.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk):
        try:
            data = JSONParser().parse(request)
            cl = Class.objects.get(name=pk)
            serializer = ClassSerializer(cl, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Class.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        try:
            cl = Class.objects.get(name=pk)
            serializer = ClassSerializer(cl)
            cl.delete()
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Class.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
