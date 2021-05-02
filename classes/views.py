from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from classes.models import Classes
from classes.serializers import ClassSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class ClassViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Classes.objects.all()
    serializer_class = ClassSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'type', 'age', 'difficulty', 'workarea', 'categories']
