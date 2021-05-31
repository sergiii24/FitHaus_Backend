from rest_framework import viewsets
from shareAchievements.models import ShareAchievement
from shareAchievements.serializers import ShareAchievementSerializer


class ShareAchievementViewSet(viewsets.ModelViewSet):
    queryset = ShareAchievement.objects.all()
    serializer_class = ShareAchievementSerializer
