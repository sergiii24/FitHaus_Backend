from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from activities.models import Activity
from activities.serializers import ActivitySerializer
from rest_framework.parsers import MultiPartParser, FormParser


class ActivitiesViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']

