from django.db import models
from predefinedroutine.models import PredefinedRoutine


class Collection(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    description = models.CharField(max_length=200)
    predef_routines = models.ManyToManyField(PredefinedRoutine, blank=True)

    def __str__(self):
        return self.name


class CollectionDTO(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    predef_routines = []

