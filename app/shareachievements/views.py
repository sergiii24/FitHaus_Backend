from rest_framework import viewsets, status
from rest_framework.response import Response
from shareachievements.models import ShareAchievement
from shareachievements.serializers import shareachievementserializer


class ShareAchievementViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = ShareAchievement.objects.all()
        user = request.query_params.get('user')
        achievement = request.query_params.get('achievement')
        if user is not None:
            queryset = queryset.filter(user=user)
            if achievement is not None:
                queryset = queryset.filter(achievement=achievement)
        elif achievement is not None:
            queryset = queryset.filter(achievement=achievement)
        if queryset.count() > 0:
            serializer = shareachievementserializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, user, achievement, share):
        try:
            shareachievement = ShareAchievement()
            shareachievement.user = user
            shareachievement.achievement = achievement
            shareachievement.share = share
            shareachievement.save()
            serialized = shareachievementserializer(shareachievement)
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        except ShareAchievement.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        try:
            ac = ShareAchievement.objects.get(id=pk)
            serialized = shareachievementserializer(ac)
            return Response(serialized.data, status=status.HTTP_200_OK)
        except ShareAchievement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
