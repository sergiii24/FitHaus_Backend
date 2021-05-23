from rest_framework import viewsets
from achivements.models import Achievement
from achivements.serializers import AchievementSerializer


class AchievementsViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
