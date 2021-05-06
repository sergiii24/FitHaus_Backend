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
    dayhour = models.DateField()
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
