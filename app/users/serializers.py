from rest_framework import serializers
from users.models import User
from users.models import NormalUserDTO
from users.models import ExternalUserDTO
from django.core.validators import MinLengthValidator
from .validators import correct_pwd


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['strengthtrainings','cardiotrainings','yogatrainings','stretchingtrainings',
                   'rehabilitationtrainings','pilatestrainings']


class NormalUserInfoSerializer(serializers.Serializer):
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


class ExternUserInfoSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    firstname = serializers.CharField(max_length=200)
    lastname = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=200)
    uid = serializers.CharField(max_length=200)
    provider = serializers.CharField(max_length=200)

    def __init__(self, username, firstname, lastname, email, uid, provider, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.uid = uid
        self.provider = provider


class UserCreationSerializer(serializers.Serializer):
    username = serializers.CharField(validators=[MinLengthValidator(4)], max_length=200)
    firstname = serializers.CharField(max_length=200)
    lastname = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=200)



class NormalUserCreationSerializer(serializers.Serializer):
    password = serializers.CharField(validators=[MinLengthValidator(8), correct_pwd], max_length=200)
    POSIBLE_GENDERS = [
        ('M', 'Male'),
        ('W', 'Women'),
        ('X', 'Undefined')
    ]
    gender = serializers.ChoiceField(choices=POSIBLE_GENDERS)
    birthdate = serializers.DateField()


class ExternUserCreationSerializer(serializers.Serializer):
    uid = serializers.CharField()
    provider = serializers.CharField()


class UserRankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'points')


class UserStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'activitiesdone', 'achivements', 'points', 'level')


class NormalUserDTOSerializer(serializers.ModelSerializer):
    objectives = serializers.ListField(child=serializers.CharField())
    categories = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = NormalUserDTO
        exclude = ('id',)


class ExternalUserDTOSerializer(serializers.ModelSerializer):
    objectives = serializers.ListField(child=serializers.CharField())
    categories = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = ExternalUserDTO
        exclude = ('id',)
