from activities.models import Activity
from django.db import models


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
        ('Ca', 'Calf'),
        ('Co', 'Core')
    ]
    muscle = models.CharField(choices=POSIBLE_MUSCLE, max_length=200, default='Bi')


class ExerciseDTO(models.Model):
    type = models.CharField(max_length=30, default='E')
    name = models.CharField(max_length=30, default='')
    description = models.CharField(max_length=1, null=True)
    age = models.CharField(max_length=30, default='A')
    difficulty = models.CharField(max_length=30, default='M')
    length = models.IntegerField(null=True)
    categories = []
    pre = models.ImageField(upload_to='activities_images', null=True)
    muscleimage = models.ImageField(upload_to='exercise_images', default=None)
    videotutorial = models.FileField(upload_to='exercise_videos', default=None)
    videoexercise = models.FileField(upload_to='exercise_videos', default=None)
    muscle = models.CharField(max_length=1, default='Bi')
