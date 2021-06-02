from customroutines.models import CustomRoutine
from customroutines.serializers import CustomRoutineSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
# Create your views here.
from users.models import User


class CustomRoutinesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = CustomRoutine.objects.all()
        name = request.query_params.get('name')
        time = request.query_params.get('time')
        categories = request.query_params.get('categories')
        if name is not None:
            queryset = queryset.filter(name=name)
        elif time is not None:
            queryset = queryset.filter(time=time)
        elif categories is not None:
            queryset = queryset.filter(categories=categories)
        serializer = CustomRoutineSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            data = JSONParser().parse(request)
            serialized = CustomRoutineSerializer(data=data)
            if serialized.is_valid():
                cr = CustomRoutine()
                cr.name = serialized.validated_data.get('name')
                cr.description = serialized.validated_data.get('description')
                cr.time = serialized.validated_data.get('time')
                cr.public = serialized.validated_data.get('public')
                cr.user = serialized.validated_data.get('user')
                # pr.image = serialized.validated_data.get('image')
                cr.save()

                categories = []
                cat = serialized.validated_data.get('categories')
                for c in cat:
                    categories.append(c.category)
                cr.categories.set(categories)

                exercises = []
                ex = serialized.validated_data.get('exercises')
                for e in ex:
                    exercises.append(e.name)
                cr.exercises.set(exercises)

                classes = []
                cla = serialized.validated_data.get('classes')
                for c in cla:
                    classes.append(c.name)
                cr.classes.set(classes)
                cr.save()
                return Response(serialized.data, status=status.HTTP_201_CREATED)
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        except CustomRoutine.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        try:
            cr = CustomRoutine.objects.get(id=pk)
            serialized = CustomRoutineSerializer(cr)
            return Response(serialized.data, status=status.HTTP_200_OK)
        except CustomRoutine.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)