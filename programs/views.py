from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from programs.models import Program
from programs.serializers import ProgramSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class ProgramViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'level', 'weeks']
