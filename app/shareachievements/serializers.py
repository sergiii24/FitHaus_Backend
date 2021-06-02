from rest_framework import serializers
from shareachievements.models import ShareAchievement


class shareachievementserializer(serializers.ModelSerializer):
    class Meta:
        model = ShareAchievement
        fields = '__all__'
