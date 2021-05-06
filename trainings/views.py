from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from trainings.models import Training
from trainings.serializers import TrainingSerializer

# Create your views here.


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']
