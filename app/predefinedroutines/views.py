from django_filters.rest_framework import DjangoFilterBackend
from predefinedroutines.models import PredefinedRoutine
from predefinedroutines.serializers import PredfinedRoutineSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


# Create your views here.


class PredefinedRoutineViewSet(viewsets.ViewSet):
    PredefinedRoutineQuery = PredefinedRoutine.objects.all()
    queryset = PredefinedRoutineQuery
    serializer_class = PredfinedRoutineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'time', 'categories', 'age', 'level', 'equipment', 'objective', 'impact']

    def list(self, request):
        queryset = PredefinedRoutine.objects.all()
        name = request.query_params.get('name')
        time = request.query_params.get('time')
        categories = request.query_params.get('categories')
        age = request.query_params.get('age')
        level = request.query_params.get('level')
        equipment = request.query_params.get('equipment')
        objective = request.query_params.get('objective')
        impact = request.query_params.get('impact')
        if name is not None:
            queryset = queryset.filter(name=name)
        elif time is not None:
            queryset = queryset.filter(time=time)
        elif categories is not None:
            queryset = queryset.filter(categories=categories)
        elif age is not None:
            queryset = queryset.filter(age=age)
        elif level is not None:
            queryset = queryset.filter(level=level)
        elif equipment is not None:
            queryset = queryset.filter(equipment=equipment)
        elif objective is not None:
            queryset = queryset.filter(objective=objective)
        elif impact is not None:
            queryset = queryset.filter(impact=impact)
        serializer = PredfinedRoutineSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            data = JSONParser().parse(request)
            serialized = PredfinedRoutineSerializer(data=data)
            if serialized.is_valid():
                # name = serialized.validated_data.get('name')
                pr = PredefinedRoutine()
                pr.name = serialized.validated_data.get('name')
                pr.description = serialized.validated_data.get('description')
                pr.time = serialized.validated_data.get('time')
                pr.age = serialized.validated_data.get('age')
                pr.level = serialized.validated_data.get('level')
                pr.equipment = serialized.validated_data.get('equipment')
                pr.objective = serialized.validated_data.get('objective')
                pr.impact = serialized.validated_data.get('impact')
                # pr.image = serialized.validated_data.get('image')
                pr.save()

                categories = []
                cat = serialized.validated_data.get('categories')
                for c in cat:
                    categories.append(c.category)
                pr.categories.set(categories)

                exercises = []
                ex = serialized.validated_data.get('exercises')
                for e in ex:
                    exercises.append(e.name)
                pr.classes.set(exercises)

                classes = []
                cla = serialized.validated_data.get('classes')
                for c in cla:
                    classes.append(c.name)
                pr.classes.set(classes)
                pr.save()
                return Response(serialized.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except PredefinedRoutine.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
