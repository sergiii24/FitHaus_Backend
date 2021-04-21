from django.db import models


# Create your models here.

class Activity(models.Model):
    id = models.IntegerField
    POSIBLE_TYPE = [
        ('E', 'Exercise'),
        ('C', 'Class')
    ]
    type = models.CharField(max_length=30, choices=POSIBLE_TYPE, default='E')
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    POSIBLE_AGE = [
        ('K', 'Kid'),
        ('T', 'Teenager'),
        ('A', 'Adult'),
        ('E', 'Elder')
    ]
    age = models.CharField(max_length=30, choices=POSIBLE_AGE)
    POSIBLE_DIFFICULTY = [
        ('E', 'Easy'),
        ('M', 'Medium'),
        ('H', 'Hard')
    ]
    difficulty = models.CharField(max_length=30, choices=POSIBLE_DIFFICULTY)
    length = models.IntegerField()

    # pre = models.ImageField(upload_to='albums/images/')

    def __str__(self):
        return self.name




class Class(Activity):
    # video = models.CharField(max_length=2)
    trainer = models.CharField(max_length=30)
    POSIBLE_WORKAREA = [
        ('UB', 'Upper Body'),
        ('LB', 'Lower Body'),
        ('FB', 'Full Body'),
        ('C', 'Core')
    ]
    workarea = models.CharField(choices=POSIBLE_WORKAREA, max_length=200, default='FB')

