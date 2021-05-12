from django.db import models
from PredefinedRoutine.models import PredefinedRoutine
from CustomRoutine.models import CustomRoutine


class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    predef_routines = models.ManyToManyField(PredefinedRoutine, blank=True)
    custom_routines = models.ManyToManyField(CustomRoutine, blank=True)

    def __str__(self):
        return self.name

