from django.db import models
from activities.models import Activity


# Create your models here.
class Exercise(models.Model):
    activity = models.OneToOneField(Activity, primary_key=True, on_delete=models.CASCADE)
    video = models.CharField(max_length=2)
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