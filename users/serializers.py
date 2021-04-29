from django.core.exceptions import ValidationError
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserRankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'points')
