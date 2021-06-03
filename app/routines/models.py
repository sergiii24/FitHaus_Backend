from categories.models import Category
from classes.models import Class
from django.db import models
from exercises.models import Exercise


# Create your models here.

class Routine(models.Model):
    name = models.CharField(max_length=100, default=None)
    description = models.CharField(max_length=500)
    POSIBLE_TIME = [
        ('P', 'Personalitzable'),
        ('R', 'Ronda circuits'),
        ('F', 'Fixat')
    ]
    time = models.CharField(max_length=30, choices=POSIBLE_TIME, default='F')
    categories = models.ManyToManyField(Category, default=None)
    exercises = models.ManyToManyField(Exercise, blank=True, default=None)
    classes = models.ManyToManyField(Class, blank=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
