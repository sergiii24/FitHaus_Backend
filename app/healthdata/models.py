import datetime

from computed_property import ComputedFloatField
from django.db import models
from users.models import User


class HealthData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    weight = ComputedFloatField(compute_from='calc_weight', default=1)
    height = ComputedFloatField(compute_from='calc_height', default=1)
    imc = ComputedFloatField(compute_from='calc_imc', default=1)
    igc = ComputedFloatField(compute_from='calc_igc', default=1)
    date = models.DateField(auto_now=True)

    @property
    def calc_weight(self):
        weight = self.user.weight
        return weight

    @property
    def calc_height(self):
        height = self.user.height
        return height

    @property
    def calc_imc(self):
        imc = self.user.weight / ((self.user.height / 100) * (self.user.height / 100))
        return imc

    @property
    def calc_igc(self):
        edat = datetime.date.today().year - self.user.birthdate.year
        sexe = ('M' == self.user.gender)
        if edat < 16:
            if sexe:
                igc = 1.51 * self.imc - 0.7 * edat - 3.6 + 1.4
            else:
                igc = 1.51 * self.imc - 0.7 * edat + 1.4
        else:
            if sexe:
                igc = 1.39 * self.imc + 0.16 * edat - 10.34 - 9
            else:
                igc = 1.39 * self.imc + 0.16 * edat - 9
        return igc


class HealthDataDTO(models.Model):
    user_id = models.IntegerField(default=None)
    weight = models.FloatField(default=1)
    height = models.FloatField(default=1)
    imc = models.FloatField(default=1)
    igc = models.FloatField(default=1)
    date = models.DateField()
