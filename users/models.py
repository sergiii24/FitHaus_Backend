from django.core.validators import MinLengthValidator
from django.db import models
from .validators import correct_pwd


# Create your models here.
class User(models.Model):
    # DADES PERSONALS
    id = models.IntegerField
    username = models.CharField(validators=[MinLengthValidator(4)], max_length=200, unique=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(validators=[MinLengthValidator(8), correct_pwd], max_length=200)

    POSIBLE_GENDERS = [
        ('M', 'Male'),
        ('W', 'Women'),
        ('X', 'Undefined')
    ]
    gender = models.CharField(max_length=1, choices=POSIBLE_GENDERS)
    birthdate = models.DateField()
    # DADES ESPORTIVES
    activitiesdone = models.IntegerField(default=0)
    achivements = models.CharField(max_length=200)
    points = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    objective = models.CharField(max_length=200)
    interestcategories = models.CharField(max_length=200)
    # DADES FISIQUES
    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)
    imc = models.IntegerField(default=0)
    igc = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True) #DATA DARRERA MODIFICACIO

    # historical????????


    def __str__(self):
        return self.id

