from django.db import models
from routines.models import Routine


# Create your models here.

class CustomRoutine(Routine):
    public = models.BooleanField(default=False)

