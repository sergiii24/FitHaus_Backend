from activities.models import Activity
from django.db import models


class Class(Activity):
    videoclass = models.FileField(upload_to='class_videos', default=None)
    trainer = models.CharField(max_length=30)
    POSIBLE_WORKAREA = [
        ('UB', 'Upper Body'),
        ('LB', 'Lower Body'),
        ('FB', 'Full Body'),
        ('C', 'Core')
    ]
    workarea = models.CharField(choices=POSIBLE_WORKAREA, max_length=200, default='FB')


class ClassDTO(models.Model):
    type = models.CharField(max_length=30, default='E')
    name = models.CharField(max_length=30, default='')
    description = models.CharField(max_length=1, null=True)
    age = models.CharField(max_length=30, default='A')
    difficulty = models.CharField(max_length=30, default='M')
    length = models.IntegerField(null=True)
    categories = []
    pre = models.ImageField(upload_to='activities_images', null=True)
    videoclass = models.FileField(upload_to='class_videos', default=None)
    trainer = models.CharField(max_length=30)
    workarea = models.CharField(max_length=200, default='FB')
