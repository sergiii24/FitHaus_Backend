from django.core.exceptions import ValidationError
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    #def validate(self, attrs):
    #    user = User(**attrs)
    #    if user.Nobjectives > 4 or user.Ncategories > 4:
    #        return attrs
    #    raise ValidationError("Users must have no more than 3 objectives or categories")

    class Meta:
        model = User
        fields = '__all__'
