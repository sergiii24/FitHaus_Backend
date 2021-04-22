from rest_framework import viewsets
from routines.models import Routine
from routines.serializers import RoutineSerializer
from django_filters.rest_framework import DjangoFilterBackend


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'time']
