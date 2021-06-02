from rest_framework import viewsets, status
from rest_framework.response import Response
from shareachievements.models import ShareAchievement
from shareachievements.serializers import shareachievementserializer


class ShareAchievementViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = ShareAchievement.objects.all()
        achievement = request.query_params.get('achievement')
        quantity = request.query_params.get('quantity')
        if achievement is not None:
            queryset = queryset.filter(achievement=achievement)
            if quantity is not None:
                queryset = queryset.filter(quantity=quantity)
        elif quantity is not None:
            queryset = queryset.filter(quantity=quantity)
        serializer = shareachievementserializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
