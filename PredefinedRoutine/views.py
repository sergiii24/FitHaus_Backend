from PredefinedRoutine.serializers import PredfinedRoutineSerializer
from rest_framework import viewsets
from PredefinedRoutine.models import PredefinedRoutine

# Create your views here.


class PredefinedRoutineViewSet(viewsets.ModelViewSet):
    PredefinedRoutineQuery = PredefinedRoutine.objects.all()
    queryset = PredefinedRoutineQuery
    serializer_class = PredfinedRoutineSerializer