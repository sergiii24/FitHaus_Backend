import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from trainings.models import Training
from trainings.serializers import TrainingSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from users.models import User

# Create your views here.


class TrainingViewSet(viewsets.ViewSet):

    def list(self, request):
        #today = datetime.date.today()
        #today_day = today.day
        #if today_day == 31:
        #    today_day = 30
        #today_month = today.month
        #today_year = today.year

        #queryset = Training.objects.filter(date__range=[today, str(today_year) + "-" + str(today_month + 1) + "-" + str(
                                                            #today_day)])
        queryset = Training.objects.all()
        user = request.query_params.get('user')
        if user is not None:
            queryset = queryset.filter(user=user)
        serializer = TrainingSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            data = JSONParser().parse(request)
            serialized = TrainingSerializer(data=data)
            if serialized.is_valid():
                tr = Training.objects.create(user=serialized.validated_data.get('user'),
                                             customroutine=serialized.validated_data.get('customroutine'),
                                             predefinedroutine=serialized.validated_data.get('predefinedroutine'),
                                             date=serialized.validated_data.get('date'),
                                             hInici=serialized.validated_data.get('hInici'),
                                             hFi=serialized.validated_data.get('hFi'))
                tr.done = serialized.validated_data.get('done')
                tr.shared = serialized.validated_data.get('shared')
                tr.save()
                return Response(serialized.data, status=status.HTTP_201_CREATED)
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        except Training.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        try:
            tr = Training.objects.get(id=pk)
            serialized = TrainingSerializer(tr)
            return Response(serialized.data, status=status.HTTP_200_OK)
        except Training.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        try:
            data = JSONParser().parse(request)
            tr = Training.objects.get(id=pk)
            serializer = TrainingSerializer(tr, data=data, partial=True)
            if serializer.is_valid():
                if data.get('done'):
                    tr.done = serializer.validated_data.get('done')
                    serializer.update(tr.user, tr.predefinedroutine)
                    tr.user.achievement()
                if data.get('shared'):
                    tr.shared = serializer.validated_data.get('shared')
                tr.save()
                serializer = TrainingSerializer(tr)
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Training.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)