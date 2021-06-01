from rest_framework import viewsets, status
from healthData.models import HealthData, HealthDataDTO
from healthData.serializers import HealthDataSerializer, HealthDataDTOSerializer
from rest_framework.response import Response
from users.models import User
from rest_framework.parsers import JSONParser
import datetime


class HealthDataViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = HealthData.objects.all()
        id = request.query_params.get('userid')
        if id is not None:
            user = User.objects.get(id=id)
            queryset = queryset.filter(user=user)
        serializer = HealthDataSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            data = JSONParser().parse(request)
            pk = data.get('userid')
            user = User.objects.get(id=pk)
            if user is not None:
                hd = HealthData()
                hd.user = user
                hd.save()
                hdto = HealthDataDTO(id=hd.id,
                                     username=user.username,
                                     weight=user.weight,
                                     height=user.height,
                                     imc=1,
                                     igc=1,
                                     date=datetime.date.today())
                serialized = HealthDataDTOSerializer(hdto)
                return Response(serialized.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)