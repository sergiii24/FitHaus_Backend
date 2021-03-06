from achievements.models import Achievement
from achievements.serializers import AchievementSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


class AchievementsViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Achievement.objects.all()
        achievement = request.query_params.get('achievement')
        quantity = request.query_params.get('quantity')
        if achievement is not None:
            queryset = queryset.filter(achievement=achievement)
            if quantity is not None:
                queryset = queryset.filter(quantity=quantity)
        elif quantity is not None:
            queryset = queryset.filter(quantity=quantity)
        if queryset.count() > 0:
            serializer = AchievementSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        try:
            data = JSONParser().parse(request)
            serialized = AchievementSerializer(data=data)
            if serialized.is_valid():
                achievement = Achievement()
                achievement.achievement = serialized.validated_data.get('achievement')
                achievement.quantity = serialized.validated_data.get('quantity')
                achievement.points = serialized.validated_data.get('points')
                achievement.save()
                return Response(serialized.data, status=status.HTTP_201_CREATED)
        except Achievement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk):
        try:
            ac = Achievement.objects.get(id=pk)
            serialized = AchievementSerializer(ac)
            return Response(serialized.data, status=status.HTTP_200_OK)
        except Achievement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
