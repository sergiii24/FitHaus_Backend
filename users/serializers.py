from rest_framework import serializers
from users.models import User


class SnippetSerializer(serializers.Serializer):
    # DADES PERSONALS
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    mail = serializers.CharField(read_only=True)
    password = serializers.CharField(read_only=True)
    gender = serializers.CharField(read_only=True)
    birthDate = serializers.DateField(read_only=True)
    #DADES ESPORTIVES
    activitiesDone = serializers.IntegerField(read_only=True)
    #archivements =
    points = serializers.IntegerField(read_only=True)
    level = serializers.IntegerField(read_only=True)
    objective = serializers.CharField(read_only=True)
    #interestCategories = #?????
    #DADES FISIQUES
    weight = serializers.IntegerField(read_only=True)
    height = serializers.IntegerField(read_only=True)
    imc = serializers.IntegerField(read_only=True)
    igc = serializers.IntegerField(read_only=True)
    # historic????????

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #DADES PERSONALS
        id = validated_data.get('id', instance.id)
        name = validated_data.get('name', instance.name)
        mail = validated_data.get('mail', instance.mail)
        password = validated_data.get('password', instance.password)
        gender = validated_data.get('gender', instance.gender)
        birthdate = validated_data.get('birthDate', instance.birthdate)
        #DADES ESPORTIVES
        activitiesdone = validated_data.get('activitiesDone', instance.activitiesdone)
        #archivements = ???
        points = validated_data.get('points', instance.points)
        level = validated_data.get('level', instance.level)
        objective = validated_data.get('objective', instance.objective)
        #interestcategories = ?????
        #DADES FISIQUES
        weight = validated_data.get('weight', instance.weight)
        height = validated_data.get('height', instance.height)
        imc = validated_data.get('imc', instance.imc)
        igc = validated_data.get('igc', instance.igc)
        # historical????????

        instance.save()
        return instance