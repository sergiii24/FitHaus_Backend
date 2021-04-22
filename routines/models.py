from django.core.exceptions import ValidationError
from django.db import models

from categories.models import Category
from exercises.models import Exercise
from classes.models import Classes
from django.db.models.signals import m2m_changed


# Create your models here.

class Routine(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)
    POSIBLE_TIME = [
        ('P', 'Personalitzable'),
        ('R', 'Ronda circuits'),
        ('F', 'Fixat')
    ]
    time = models.CharField(max_length=30, choices=POSIBLE_TIME, default='F')
    categories = models.ManyToManyField(Category)
    exercises = models.ManyToManyField(Exercise)
    classes = models.ManyToManyField(Classes, blank=True)

    def __str__(self):
        return self.name


def is_correct(sender, action, **kwargs):
    if action == "pre_add":
        instance = kwargs.pop('instance', None)
        instance.name = "JJJ"
        if instance.exercises.exists() & instance.classes.exists():
            raise ValidationError("ERROR")
        instance.save()


m2m_changed.connect(is_correct, sender=[Routine.exercises.through, Routine.classes.through])
