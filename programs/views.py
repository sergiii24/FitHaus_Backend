from rest_framework import viewsets
from programs.models import Program
from programs.serializers import ProgramSerializer


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
