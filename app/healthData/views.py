from rest_framework import viewsets, status
from healthData.models import HealthData
from healthData.serializers import HealthDataSerializer
from rest_framework.response import Response
from users.models import User


class HealthDataViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = HealthData.objects.all()
        id = request.query_params.get('userid')
        if id is not None:
            user = User.objects.get(id=id)
            queryset = queryset.filter(user=user)
        serializer = HealthDataSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
