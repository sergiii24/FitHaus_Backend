from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from classes.models import Classes
from classes.serializers import ClassSerializer


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['trainer', 'workarea']
