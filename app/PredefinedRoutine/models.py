from django.db import models

from objectives.models import Objective
from routines.models import Routine
from users.models import User


# Create your models here.


class PredefinedRoutine(Routine):
    POSIBLE_AGE = [
        ('K', 'Kid'),
        ('T', 'Teenager'),
        ('A', 'Adult'),
        ('E', 'Elder')
    ]
    age = models.CharField(max_length=30, choices=POSIBLE_AGE, default='A')
    POSIBLE_LEVEL = [
        ('P', 'Principiate'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    ]
    level = models.CharField(max_length=30, choices=POSIBLE_LEVEL, default='P')
    POSIBLE_EQUIPMENT = [
        ('W', 'Without'),
        ('HM', 'HomeMaterial'),
        ('K', 'Kettlebelt'),
        ('B', 'Bodyweight'),
        ('D', 'Dumpbell'),
        ('RB', 'ResistanceBand'),
        ('RL', 'ResistanceLoop'),
        ('FR', 'FoamRoller')
    ]
    equipment = models.CharField(max_length=30, choices=POSIBLE_EQUIPMENT, default='W')
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE, default=None)
    POSIBLE_IMPACT = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    impact = models.CharField(max_length=30, choices=POSIBLE_IMPACT, default='M')
    image = models.ImageField(upload_to='predef_routines_images', default=None)
    #users = models.ManyToManyField(User)

