from rest_framework import serializers
from users.models import User
from django.db import models
from django.core.validators import MinLengthValidator
from .validators import correct_pwd


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class UserCreationSerializer(serializers.Serializer):
    username = serializers.CharField(validators=[MinLengthValidator(4)], max_length=200)
    firstname = serializers.CharField(max_length=200)
    lastname = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=200)
    password = serializers.CharField(validators=[MinLengthValidator(8), correct_pwd], max_length=200)
    POSIBLE_GENDERS = [
        ('M', 'Male'),
        ('W', 'Women'),
        ('X', 'Undefined')
    ]
    gender = serializers.ChoiceField(choices=POSIBLE_GENDERS)
    birthdate = serializers.DateField()


class UserRankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'points')


class UserStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'activitiesdone', 'achivements', 'points', 'level')

