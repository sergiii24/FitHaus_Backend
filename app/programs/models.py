from django.db import models
from PredefinedRoutine.models import PredefinedRoutine
from CustomRoutine.models import CustomRoutine


class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    POSIBLE_LEVELS = [
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    ]
    level = models.CharField(max_length=1, choices=POSIBLE_LEVELS, default='B')
    weeks = models.IntegerField(default=0)
    predef_routines = models.ManyToManyField(PredefinedRoutine, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'level')