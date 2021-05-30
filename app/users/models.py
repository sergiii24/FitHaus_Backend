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
    points = models.IntegerField(default=0)
    POSIBLE_LEVELS = [
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    ]
    level = models.CharField(max_length=1, choices=POSIBLE_LEVELS, blank=True)
    objectives = models.ManyToManyField(Objective, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    # DADES FISIQUES
    weight = models.FloatField(default=0, validators=[MinValueValidator(1)])
    height = models.FloatField(default=0, validators=[MinValueValidator(1)])


    @property
    def calc_age(self):
        today = datetime.date.today()
        return today.year - self.birthdate.year

    @property
    def estadisticas(self):
        ad = self.activitiesdone
        ach = self.achivements
        p = self.points
        lvl = self.level
        stats = [ad, ach, p, lvl]
        return stats

    def __str__(self):
        return self.username


#class UserCreation(models.Model):
    # DADES PERSONALS

