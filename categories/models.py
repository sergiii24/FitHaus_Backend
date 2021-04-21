from django.db import models


class Category(models.Model):
    POSIBLE_CATEGORY = [
        ('S', 'Strength'),
        ('C', 'Cardio'),
        ('Y', 'Yoga'),
        ('E', 'Stretching'),
        ('R', 'Rehabilitation'),
        ('P', 'Pilates')
    ]
    category = models.CharField(choices=POSIBLE_CATEGORY, max_length=30, default='S', unique=True)
