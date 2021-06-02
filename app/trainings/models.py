from computed_property import ComputedIntegerField
from customroutines.models import CustomRoutine
from django.db import models
from predefinedroutines.models import PredefinedRoutine
from users.models import User
import datetime


class Training(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customroutine = models.ForeignKey(CustomRoutine, on_delete=models.CASCADE, null=True)
    predefinedroutine = models.ForeignKey(PredefinedRoutine, on_delete=models.CASCADE, null=True)
    date = models.DateField(default=None)
    hInici = models.TimeField(null=True)
    hFi = models.TimeField(null=True)
    totalTime = ComputedIntegerField(compute_from='calc_hours')
    done = models.BooleanField(default=False)
    shared = models.BooleanField(default=False)

    @property
    def calc_hours(self):
        horaIni = self.hInici.hour
        horaFi = self.hFi.hour
        return horaIni - horaFi
