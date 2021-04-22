from django.db import models
from activities.models import Activity


# Create your models here.
class Exercise(models.Model):
    activity = models.OneToOneField(Activity, on_delete=models.CASCADE, related_name='exercise2activity')
    #video = models.FileField
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