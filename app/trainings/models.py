from django.db import models
from computed_property import ComputedIntegerField
from CustomRoutine.models import CustomRoutine
from PredefinedRoutine.models import PredefinedRoutine
from routines.models import Routine
from users.models import User


class Training(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customroutine = models.ForeignKey(CustomRoutine, on_delete=models.CASCADE, null=True)
    predefinedroutine = models.ForeignKey(PredefinedRoutine, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    hInici = models.TimeField()
    hFi = models.TimeField()
    totalTime = ComputedIntegerField(compute_from='calc_hours')
    done = models.BooleanField()
    shared = models.BooleanField()

    @property
    def calc_hours(self):
        horaIni = self.hInici.hour
        horaFi = self.hFi.hour
        return horaIni - horaFi

    def save(self, *args, **kwargs):
        cats = self.customroutine.categories
        for c in cats.items():
            if c == "S":
                us, updated = User.objects.update_or_create(
                    strengthtrainings=self.user.strengthtrainings + 1
                )
            elif c == "C":
                us, updated = User.objects.update_or_create(
                    cardiotrainings=self.user.cardiotrainings + 1
                )
            elif c == "Y":
                us, updated = User.objects.update_or_create(
                    yogatrainings=self.user.yogatrainings + 1
                )
            elif c == "E":
                us, updated = User.objects.update_or_create(
                    stretchingtrainings=self.user.stretchingtrainings + 1
                )
            elif c == "R":
                us, updated = User.objects.update_or_create(
                    rehabilitationtrainings=self.user.rehabilitationtrainings + 1
                )
            elif c == "P":
                us, updated = User.objects.update_or_create(
                    pilatestrainings=self.user.pilatestrainings + 1
                )
        return super().save(*args, **kwargs)
