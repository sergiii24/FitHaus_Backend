from django.db import models


class Achievement(models.Model):
    POSIBLE_ACHIEVEMENTS = [
        ('TT', 'Total Trainings'),
        ('ST', 'Strength Trainings'),
        ('CT', 'Cardio Trainings'),
        ('YT', 'Yoga Trainings'),
        ('StchT', 'Stretching Trainings'),
        ('RT', 'Rehabilitation Trainings'),
        ('PT', 'Pilates Trainings'),
    ]
    achievement = models.CharField(max_length=10, choices=POSIBLE_ACHIEVEMENTS)
    quantity = models.IntegerField(default=1)
    Points = models.IntegerField(default=1)