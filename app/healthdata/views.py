from healthdata.models import HealthData, HealthDataDTO
from healthdata.serializers import HealthDataSerializer, HealthDataDTOSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from users.models import User


class HealthDataViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = HealthData.objects.all()
        id = request.query_params.get('userid')
        if id is not None:
            user = User.objects.get(id=id)
            queryset = queryset.filter(user=user)
        if queryset.count() > 0:
            serializer = HealthDataSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        try:
            data = JSONParser().parse(request)
            pk = data.get('userid')
            user = User.objects.get(id=pk)
            if user is not None:
                hd = HealthData.objects.create(user=user)
                hd.save()
                hdto = HealthDataDTO(id=hd.id,
                                     user_id=user.id,
                                     weight=user.weight,
                                     height=user.height,
                                     imc=hd.imc,
                                     igc=hd.igc,
                                     date=hd.date)
                serialized = HealthDataDTOSerializer(hdto)
                return Response(serialized.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk):
        try:
            hd = HealthData.objects.get(id=pk)
            user = User.objects.get(id=hd.user.id)
            hdto = HealthDataDTO(id=hd.id,
                                 user_id=user.id,
                                 weight=user.weight,
                                 height=user.height,
                                 imc=hd.imc,
                                 igc=hd.igc,
                                 date=hd.date)
            serialized = HealthDataDTOSerializer(hdto)
            return Response(serialized.data, status=status.HTTP_200_OK)
        except HealthData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
