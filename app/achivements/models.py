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
    points = models.IntegerField(default=1)

    def __str__(self):
        return self.achievement

    class Meta:
        unique_together = ['achievement', 'quantity']
