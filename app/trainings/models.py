from CustomRoutine.models import CustomRoutine
from computed_property import ComputedIntegerField
from django.db import models
from predefinedroutine.models import PredefinedRoutine
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

