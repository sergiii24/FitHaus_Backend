from rest_framework import viewsets
from healthData.models import HealthData
from healthData.serializers import HealthDataSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = HealthData.objects.all()
    serializer_class = HealthDataSerializer
