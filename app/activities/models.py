from categories.models import Category
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

class Activity(models.Model):
    POSIBLE_TYPE = [
        ('E', 'Exercise'),
        ('C', 'Class')
    ]
    type = models.CharField(max_length=30, choices=POSIBLE_TYPE, default='E')
    name = models.CharField(max_length=50, primary_key=True, default='')
    description = models.CharField(max_length=500, null=True)
    POSIBLE_AGE = [
        ('K', 'Kid'),
        ('T', 'Teenager'),
        ('A', 'Adult'),
        ('E', 'Elder')
    ]
    age = models.CharField(max_length=30, choices=POSIBLE_AGE, default='A')
    POSIBLE_DIFFICULTY = [
        ('E', 'Easy'),
        ('M', 'Medium'),
        ('H', 'Hard')
    ]
    difficulty = models.CharField(max_length=30, choices=POSIBLE_DIFFICULTY, default='M')
    length = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    categories = models.ManyToManyField(Category)
    pre = models.ImageField(upload_to='activities_images', null=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
