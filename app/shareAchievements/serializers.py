from rest_framework import serializers
from shareAchievements.models import ShareAchievement


class ShareAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareAchievement
        fields = '__all__'
