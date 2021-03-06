import datetime

from achievements.models import Achievement
from categories.models import Category
from computed_property import ComputedFloatField
from computed_property import ComputedIntegerField
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator
from django.db import models
from objectives.models import Objective

from .validators import correct_pwd


# Create your models here.
class User(models.Model):
    # DADES PERSONALS
    id = models.IntegerField
    username = models.CharField(validators=[MinLengthValidator(4)], max_length=200, unique=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    POSIBLE_GENDERS = [
        ('M', 'Male'),
        ('W', 'Women'),
        ('X', 'Undefined')
    ]
    gender = models.CharField(max_length=1, choices=POSIBLE_GENDERS, blank=True)
    birthdate = models.DateField(null=True)
    # DADES ESPORTIVES
    activitiesdone = ComputedIntegerField(compute_from='calc_routines')
    points = models.IntegerField(default=0)
    POSIBLE_LEVELS = [
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    ]
    level = models.CharField(max_length=1, choices=POSIBLE_LEVELS)
    objectives = models.ManyToManyField(Objective)
    categories = models.ManyToManyField(Category)
    strengthtrainings = models.IntegerField(default=0)
    cardiotrainings = models.IntegerField(default=0)
    yogatrainings = models.IntegerField(default=0)
    stretchingtrainings = models.IntegerField(default=0)
    rehabilitationtrainings = models.IntegerField(default=0)
    pilatestrainings = models.IntegerField(default=0)
    # DADES FISIQUES
    weight = models.FloatField(default=1, validators=[MinValueValidator(1)])
    height = models.FloatField(default=1, validators=[MinValueValidator(1)])
    imc = ComputedFloatField(compute_from='calc_imc', default=1)
    igc = ComputedFloatField(compute_from='calc_igc', default=1)

    @property
    def calc_routines(self):
        activities = self.strengthtrainings + self.cardiotrainings + self.yogatrainings + self.stretchingtrainings \
                     + self.rehabilitationtrainings + self.pilatestrainings
        return activities

    @property
    def calc_imc(self):
        if self.birthdate is None:
            return 1
        imc = self.weight / ((self.height / 100) * (self.height / 100))
        return imc

    @property
    def calc_igc(self):
        if self.birthdate is None:
            return 1
        edat = datetime.date.today().year - self.birthdate.year
        sexe = ('M' == self.gender)
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

    @property
    def estadisticas(self):
        ad = self.activitiesdone
        # ach = self.achievements
        p = self.points
        lvl = self.level
        stats = [ad, ach, p, lvl]
        return stats

    def get_normal_user(self):
        if hasattr(self, 'normal_user'):
            return self.normal_user
        return None

    def achievement(self):
        from shareachievements.models import ShareAchievement
        if (((self.activitiesdone + 1) % 10) == 0) and (self.activitiesdone > 0):
            achi = Achievement.objects.get(achievement='TT', quantity=self.activitiesdone)
            if not ShareAchievement.objects.filter(user=self, achievement=achi):
                ShareAchievement.objects.create(user=self, achievement=achi, share=False)

        if (((self.strengthtrainings + 1) % 10) == 0) and (self.strengthtrainings > 0):
            achi = Achievement.objects.get(achievement='ST', quantity=self.strengthtrainings)
            if not ShareAchievement.objects.filter(user=self, achievement=achi):
                ShareAchievement.objects.create(user=self, achievement=achi, share=False)

        if (((self.cardiotrainings + 1) % 10) == 0) and (self.cardiotrainings > 0):
            achi = Achievement.objects.get(achievement='CT', quantity=self.cardiotrainings)
            if not ShareAchievement.objects.filter(user=self, achievement=achi):
                ShareAchievement.objects.create(user=self, achievement=achi, share=False)

        if (((self.yogatrainings + 1) % 10) == 0) and (self.yogatrainings > 0):
            achi = Achievement.objects.get(achievement='YT', quantity=self.yogatrainings)
            if not ShareAchievement.objects.filter(user=self, achievement=achi):
                ShareAchievement.objects.create(user=self, achievement=achi, share=False)

        if (((self.stretchingtrainings + 1) % 10) == 0) and (self.stretchingtrainings > 0):
            achi = Achievement.objects.get(achievement='StchT', quantity=self.stretchingtrainings)
            if not ShareAchievement.objects.filter(user=self, achievement=achi):
                ShareAchievement.objects.create(user=self, achievement=achi, share=False)

        if (((self.rehabilitationtrainings + 1) % 10) == 0) and (self.rehabilitationtrainings > 0):
            achi = Achievement.objects.get(achievement='RT', quantity=self.rehabilitationtrainings)
            if not ShareAchievement.objects.filter(user=self, achievement=achi):
                ShareAchievement.objects.create(user=self, achievement=achi, share=False)

        if (((self.pilatestrainings + 1) % 10) == 0) and (self.pilatestrainings > 0):
            achi = Achievement.objects.get(achievement='PT', quantity=self.pilatestrainings)
            if not ShareAchievement.objects.filter(user=self, achievement=achi):
                ShareAchievement.objects.create(user=self, achievement=achi, share=False)

        return self

    def __str__(self):
        return self.username


class NormalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="normal_user")
    password = models.CharField(validators=[MinLengthValidator(8), correct_pwd], max_length=200, blank=True)


class ExternUser(models.Model):
    uid = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="extern_user", primary_key=True)


class NormalUserDTO(models.Model):
    id = models.IntegerField
    username = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=1)
    birthdate = models.DateField()
    activitiesdone = models.IntegerField()
    points = models.IntegerField()
    level = models.CharField(max_length=1, blank=True)
    objectives = []
    categories = []
    weight = models.FloatField(default=1, validators=[MinValueValidator(1)])
    height = models.FloatField(default=1, validators=[MinValueValidator(1)])
    imc = models.FloatField(default=1)
    igc = models.FloatField(default=1)


class ExternalUserDTO(models.Model):
    id = models.IntegerField
    username = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    gender = models.CharField(max_length=1, blank=True)
    birthdate = models.DateField(blank=True)
    activitiesdone = models.IntegerField()
    points = models.IntegerField()
    level = models.CharField(max_length=1, blank=True)
    objectives = []
    categories = []
    weight = models.FloatField(default=1)
    height = models.FloatField(default=1)
    imc = models.FloatField(default=1)
    igc = models.FloatField(default=1)
    uid = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)
