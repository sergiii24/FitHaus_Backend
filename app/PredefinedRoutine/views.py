from django_filters.rest_framework import DjangoFilterBackend

from PredefinedRoutine.serializers import PredfinedRoutineSerializer
from rest_framework import viewsets
from PredefinedRoutine.models import PredefinedRoutine

# Create your views here.


class PredefinedRoutineViewSet(viewsets.ModelViewSet):
    PredefinedRoutineQuery = PredefinedRoutine.objects.all()
    queryset = PredefinedRoutineQuery
    serializer_class = PredfinedRoutineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'time', 'categories', 'age', 'level', 'equipment', 'objective', 'impact']