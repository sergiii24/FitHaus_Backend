from django.db import models
from users.models import User
from computed_property import ComputedFloatField
from computed_property import ComputedIntegerField
import datetime


class HealthData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    weight = ComputedIntegerField(compute_from='calc_weight', default=1)
    height = ComputedIntegerField(compute_from='calc_height', default=1)
    imc = ComputedFloatField(compute_from='calc_imc')
    igc = ComputedFloatField(compute_from='calc_igc')
    date = models.DateTimeField(auto_now=True)

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

    class Meta:
        unique_together = ('user', 'date')
        ordering = ['id']