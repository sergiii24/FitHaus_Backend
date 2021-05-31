from django.core.validators import MinLengthValidator
from django.db import models
from .validators import correct_pwd
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
    POSIBLE_GENDERS = [
        ('M', 'Male'),
        ('W', 'Women'),
        ('X', 'Undefined')
    ]
    gender = models.CharField(max_length=1, choices=POSIBLE_GENDERS, blank=True)
    birthdate = models.DateField(null=True)
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
    weight = models.FloatField(default=1, validators=[MinValueValidator(1)])
    height = models.FloatField(default=1, validators=[MinValueValidator(1)])

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

    def get_normal_user(self):
        if hasattr(self, 'normal_user'):
            return self.normal_user
        return None

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
    objectives = models.ManyToManyField(Objective, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    weight = models.FloatField(default=1, validators=[MinValueValidator(1)])
    height = models.FloatField(default=1, validators=[MinValueValidator(1)])


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
    uid = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)