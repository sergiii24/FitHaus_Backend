from django.db import models
from routines.models import Routine
from users.models import User


# Create your models here.

class CustomRoutine(Routine):
    public = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

