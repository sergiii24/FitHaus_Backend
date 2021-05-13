from django.core.validators import MinLengthValidator
from django.db import models
from .validators import correct_pwd
from computed_property import ComputedFloatField
from django.core.validators import MinValueValidator
from objectives.models import Objective
from categories.models import Category
import datetime


# Create your models here.
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
    # DADES ESPORTIVES
    activitiesdone = models.IntegerField(default=0)
    achivements = models.CharField(max_length=200)
    points = models.IntegerField(default=0)
    POSIBLE_LEVELS = [
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    ]
    level = models.IntegerField(max_length=1, choices=POSIBLE_LEVELS)
    objectives = models.ManyToManyField(Objective)
    categories = models.ManyToManyField(Category)
    # DADES FISIQUES
    weight = models.FloatField(default=0, validators=[MinValueValidator(1)])
    height = models.FloatField(default=0, validators=[MinValueValidator(1)])
    imc = ComputedFloatField(compute_from='calc_imc')
    igc = ComputedFloatField(compute_from='calc_igc')
    # DATA DARRERA MODIFICACIO PERFIL
    updated = models.DateTimeField(auto_now=True)

    # historical????????

    @property
    def calc_imc(self):
        imc = self.weight / ((self.height / 100) * (self.height / 100))
        return imc

    @property
    def calc_igc(self):
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
        ach = self.achivements
        p = self.points
        l = self.level
        stats = [ad, ach, p, l]
        return stats

    def __str__(self):
        return self.username
