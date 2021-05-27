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
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE)
    POSIBLE_IMPACT = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    impact = models.CharField(max_length=30, choices=POSIBLE_IMPACT, default='M')
    image = models.ImageField(upload_to='predef_routines_images', default=None)
    users = models.ManyToManyField(User)

    def clean(self, *args, **kwargs):
        e = self
        exers = e.exercises.all
        routinecats = e.categories.all
        edat = e.age
        for exercise in exers:
            if exercise.age != edat:
                raise Exception("Model not valid: edats no coincideixen")
            exercats = exercise.categories.all
            for cateogry in routinecats:
                if cateogry not in exercats:
                    raise Exception("Model not valid: categories no coincideixen")
        cls = e.classes.all
        for clase in cls:
            if clase.age != edat:
                raise Exception("Model not valid: edats no coincideixen")
            clasecat = clase.categories.all
            for cateogry in routinecats:
                if cateogry not in clasecat:
                    raise Exception("Model not valid: categories no coincideixen")
        super(PredefinedRoutine, self).clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(PredefinedRoutine, self).save(*args, **kwargs)
