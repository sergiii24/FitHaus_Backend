from customroutines.models import CustomRoutine
from customroutines.serializers import CustomRoutineSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets


# Create your views here.


class CustomRoutinesViewSet(viewsets.ModelViewSet):
    CustomRoutinesQuery = CustomRoutine.objects.all()
    queryset = CustomRoutinesQuery
    serializer_class = CustomRoutineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'time', 'categories']
