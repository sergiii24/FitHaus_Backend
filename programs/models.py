from django.db import models
from PredefinedRoutine.models import PredefinedRoutine
from CustomRoutine.models import CustomRoutine


class Program(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)
    POSIBLE_DIFFICULTY = [
        ('E', 'Easy'),
        ('M', 'Medium'),
        ('H', 'Hard')
    ]
    difficulty = models.CharField(max_length=30, choices=POSIBLE_DIFFICULTY, default='M')
    weeks = models.IntegerField(default=0)
    predef_routines = models.ManyToManyField(PredefinedRoutine, blank=True)
    custom_routines = models.ManyToManyField(CustomRoutine, blank=True)

    def __str__(self):
        return self.name

