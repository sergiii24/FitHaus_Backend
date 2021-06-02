from objectives.models import Objective
from objectives.serializers import ObjectiveSerializer
from rest_framework import viewsets


class ObjectiveViewSet(viewsets.ModelViewSet):
    queryset = Objective.objects.all()
    serializer_class = ObjectiveSerializer
