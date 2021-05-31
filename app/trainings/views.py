from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from trainings.models import Training
from trainings.serializers import TrainingSerializer
import datetime

# Create your views here.


class TrainingViewSet(viewsets.ModelViewSet):
    #queryset = Training.objects.all()
    today = datetime.date.today()
    today_day = today.day

    if(today_day == 31):
        today_day = 30
    today_month = today.month
    today_year = today.year

    queryset = Training.objects.filter(date__range=[today,
                                        str(today_year)+"-"+str(today_month+1)+"-"+str(today_day)])
    serializer_class = TrainingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']



