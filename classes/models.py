from django.db import models
from activities.models import Activity


class Classes(models.Model):
    activity = models.OneToOneField(Activity, primary_key=True, on_delete=models.CASCADE, related_name='class2activity')
    #video = models.CharField(max_length=2)
    trainer = models.CharField(max_length=30)
    POSIBLE_WORKAREA = [
        ('UB', 'Upper Body'),
        ('LB', 'Lower Body'),
        ('FB', 'Full Body'),
        ('C', 'Core')
    ]
    workarea = models.CharField(choices=POSIBLE_WORKAREA, max_length=200, default='FB')
