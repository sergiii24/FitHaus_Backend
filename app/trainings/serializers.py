from rest_framework import serializers
from trainings.models import Training
from users.models import User


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.done = validated_data.get('done', instance.done)

        if instance.done:
            for c in instance.predefinedroutine.categories.all():
                if c.category == 'S':
                    s = instance.user.strengthtrainings + 1
                    User.objects.filter(id=instance.user.id).update(strengthtrainings=s)
                if c.category == 'C':
                    c = instance.user.cardiotrainings + 1
                    User.objects.filter(id=instance.user.id).update(cardiotrainings=c)
                if c.category == 'Y':
                    y = instance.user.yogatrainings + 1
                    User.objects.filter(id=instance.user.id).update(yogatrainings=y)
                if c.category == 'E':
                    e = instance.user.stretchingtrainings + 1
                    User.objects.filter(id=instance.user.id).update(stretchingtrainings=e)
                if c.category == 'R':
                    r = instance.user.rehabilitationtrainings + 1
                    User.objects.filter(id=instance.user.id).update(rehabilitationtrainings=r)
                if c.category == 'P':
                    p = instance.user.pilatestrainings + 1
                    User.objects.filter(id=instance.user.id).update(pilatestrainings=p)

        User.achievement(instance.user)

        return instance
