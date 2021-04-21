from django.db import models
from activities.models import Activity


class Category(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, default=None, null=True)
    POSIBLE_CATEGORY = [
        ('S', 'Strength'),
        ('C', 'Cardio'),
        ('Y', 'Yoga'),
        ('E', 'Stretching'),
        ('R', 'Rehabilitation'),
        ('P', 'Pilates')
    ]
    category = models.CharField(choices=POSIBLE_CATEGORY, max_length=30, default='S')

    class Meta:
        constraints = [models.UniqueConstraint(fields=['activity', 'category'], name='parunico')]