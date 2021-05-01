from CustomRoutine.serializers import CustomRoutineSerializer
from rest_framework import viewsets
from CustomRoutine.models import CustomRoutine

# Create your views here.


class CustomRoutinesViewSet(viewsets.ModelViewSet):
    CustomRoutinesQuery = CustomRoutine.objects.all()
    queryset = CustomRoutinesQuery
    serializer_class = CustomRoutineSerializer