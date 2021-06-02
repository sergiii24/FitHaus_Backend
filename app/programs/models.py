from django.db import models
from predefinedroutines.models import PredefinedRoutine


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


class ProgramDTO(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    level = models.CharField(max_length=1, default='B')
    weeks = models.IntegerField(default=0)
    predef_routines = []
