from achievements.models import Achievement
from django.db import models
from users.models import User


class ShareAchievement(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    achievement = models.OneToOneField(Achievement, on_delete=models.CASCADE, default=None)
    share = models.BooleanField(default=False)
