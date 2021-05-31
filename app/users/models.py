from django.core.validators import MinLengthValidator
from django.db import models
from .validators import correct_pwd
from computed_property import ComputedFloatField
from computed_property import ComputedIntegerField
from django.core.validators import MinValueValidator
from objectives.models import Objective
from categories.models import Category
from achivements.models import Achievement
import datetime


class User(models.Model):
    # DADES PERSONALS
    id = models.IntegerField
    username = models.CharField(validators=[MinLengthValidator(4)], max_length=200, unique=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(validators=[MinLengthValidator(8), correct_pwd], max_length=200)

    POSIBLE_GENDERS = [
        ('M', 'Male'),
        ('W', 'Women'),
        ('X', 'Undefined')
    ]
    gender = models.CharField(max_length=1, choices=POSIBLE_GENDERS)
    birthdate = models.DateField()
    #age = ComputedIntegerField(compute_from='calc_age')
    # DADES ESPORTIVES
    activitiesdone = models.IntegerField(default=0)
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
    weight = models.FloatField(default=0, validators=[MinValueValidator(1)])
    height = models.FloatField(default=0, validators=[MinValueValidator(1)])
    imc = ComputedFloatField(compute_from='calc_imc')
    igc = ComputedFloatField(compute_from='calc_igc')


    @property
    def calc_age(self):
        today = datetime.date.today()
        return today.year - self.birthdate.year

    @property
    def calc_activities(self):
        activities = self.strengthtrainings + self.cardiotrainings + self.yogatrainings + self.stretchingtrainings \
                     + self.rehabilitationtrainings + self.pilatestrainings
        return activities

    @property
    def estadisticas(self):
        ad = self.activitiesdone
        ach = self.achivements
        p = self.points
        lvl = self.level
        stats = [ad, ach, p, lvl]
        return stats

    def achievement(self):
        from shareAchievements.models import ShareAchievement
        if self.activitiesdone % 10 == 0:
            achievement = Achievement.objects.filter(achivement='TT', quantity=self.activitiesdone)
            ShareAchievement.objects.create(user=self, achievement=achievement, share=False)
        if self.strengthtrainings % 10 == 0:
            achievement = Achievement.objects.filter(achivement='ST', quantity=self.strengthtrainings)
            ShareAchievement.objects.create(user=self, achievement=achievement, share=False)
        if self.cardiotrainings % 10 == 0:
            achievement = Achievement.objects.filter(achivement='CT', quantity=self.cardiotrainings)
            ShareAchievement.objects.create(user=self, achievement=achievement, share=False)
        if self.yogatrainings % 10 == 0:
            achievement = Achievement.objects.filter(achivement='YT', quantity=self.yogatrainings)
            ShareAchievement.objects.create(user=self, achievement=achievement, share=False)
        if self.stretchingtrainings % 10 == 0:
            achievement = Achievement.objects.filter(achivement='StchT', quantity=self.stretchingtrainings)
            ShareAchievement.objects.create(user=self, achievement=achievement, share=False)
        if self.rehabilitationtrainings % 10 == 0:
            achievement = Achievement.objects.filter(achivement='RT', quantity=self.rehabilitationtrainings)
            ShareAchievement.objects.create(user=self, achievement=achievement, share=False)
        if self.pilatestrainings % 10 == 0:
            achievement = Achievement.objects.filter(achivement='PT', quantity=self.pilatestrainings)
            ShareAchievement.objects.create(user=self, achievement=achievement, share=False)
        return

    def __str__(self):
        return self.username
