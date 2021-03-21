from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # highlight = serializers.HyperlinkedIdentityField(view_name='user-highlight', format='html')

    class Meta:
        model = User
        fields = ['id', 'name', 'mail', 'password', 'gender', 'birthdate',
                  'activitiesdone', 'points', 'level',
                   'objective', 'weight', 'height', 'imc', 'igc']


