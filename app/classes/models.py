from django.db import models
from activities.models import Activity


class Classes(Activity):
    videoclass = models.FileField(upload_to='class_videos', default=None)
    trainer = models.CharField(max_length=30)
    POSIBLE_WORKAREA = [
        ('UB', 'Upper Body'),
        ('LB', 'Lower Body'),
        ('FB', 'Full Body'),
        ('C', 'Core')
    ]
    workarea = models.CharField(choices=POSIBLE_WORKAREA, max_length=200, default='FB')
