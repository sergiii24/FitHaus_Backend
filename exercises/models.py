from django.core.exceptions import ValidationError
from django.db import models

from activities.models import Activity


# Create your models here.


class Exercise(Activity):
    muscleimage = models.ImageField(upload_to='exercise_images', default=None)
    videotutorial = models.FileField(upload_to='exercise_videos', default=None)
    videoexercise = models.FileField(upload_to='exercise_videos', default=None)
    POSIBLE_MUSCLE = [
        ('Bi', 'Biceps'),
        ('Tr', 'Triceps'),
        ('Fa', 'Forearm'),
        ('Ch', 'Chest'),
        ('Sh', 'Shoulder'),
        ('Do', 'Dorsal'),
        ('Gl', 'Gluteus'),
        ('Fe', 'Femoral'),
        ('Qu', 'Quadriceps'),
        ('Cm', 'Calf Muscle'),
        ('Co', 'Core')
    ]
    muscle = models.CharField(choices=POSIBLE_MUSCLE, max_length=200, default='Bi')




