from rest_framework import viewsets
from activities.models import Activity
from activities.serializers import ActivitySerializer


class ActivitiesViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

