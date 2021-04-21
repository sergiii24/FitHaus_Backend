from django.db import models
from categories.models import Category
from exercises.models import Exercise
from classes.models import Classes

# Create your models here.

class Routine(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    POSIBLE_TIME = [
        ('P', 'Personalitzable'),
        ('R', 'Ronda circuits'),
        ('F', 'Fixat')
    ]
    time = models.CharField(max_length=30, choices=POSIBLE_TIME, default='F')
    categories = models.ManyToManyField(Category)
    exercises = models.ManyToManyField(Exercise)
    classes = models.ManyToManyField(Classes)

    def __str__(self):
        return self.name