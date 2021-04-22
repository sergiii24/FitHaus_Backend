from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from objectives.models import Objective
from objectives.serializers import ObjectiveSerializer


class ObjectiveViewSet(viewsets.ModelViewSet):
    queryset = Objective.objects.all()
    serializer_class = ObjectiveSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['objective']