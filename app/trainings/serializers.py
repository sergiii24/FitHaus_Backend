from django.core.exceptions import ValidationError
from rest_framework import serializers
from trainings.models import Training
from users.models import User
from categories.models import Category


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'

    def update(self, user, predefinedroutine):
        for c in predefinedroutine.categories.all():
            if c.category == 'S':
                s = user.strengthtrainings + 1
                User.objects.filter(id=user.id).update(strengthtrainings=s)
            if c.category == 'C':
                c = user.cardiotrainings + 1
                User.objects.filter(id=user.id).update(cardiotrainings=c)
            if c.category == 'Y':
                y = user.yogatrainings + 1
                User.objects.filter(id=user.id).update(yogatrainings=y)
            if c.category == 'E':
                e = user.stretchingtrainings + 1
                User.objects.filter(id=user.id).update(stretchingtrainings=e)
            if c.category == 'R':
                r = user.rehabilitationtrainings + 1
                User.objects.filter(id=user.id).update(rehabilitationtrainings=r)
            if c.category == 'P':
                p = user.pilatestrainings + 1
                User.objects.filter(id=user.id).update(pilatestrainings=p)

        return self
