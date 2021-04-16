from django.db import models

# Create your models here.
class User(models.Model):
    #DADES PERSONALS
    id = models.IntegerField
    username = models.CharField(max_length=200, unique=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    #check has lower and uppercase letter
    #any(char.isupper() for char in password) and any(char.islower() for char in password)
    # check has at least 1 number and at least 1 not alphanumeric char
    #any(char.isnumeric() for char in password) and any(not char.isalpha() for char in password)
    POSIBLE_GENDERS = [
        ('M', 'Male'),
        ('W', 'Women'),
        ('X', 'Undefined')
    ]
    gender = models.CharField(max_length=200, choices=POSIBLE_GENDERS)
    birthdate = models.DateField()
    #DADES ESPORTIVES
    activitiesdone = models.IntegerField(default=0)
    achivements = models.CharField(max_length=200)
    points = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    objective = models.CharField(max_length=200)
    interestcategories = models.CharField(max_length=200)
    #DADES FISIQUES
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    imc = models.IntegerField(default=0)
    igc = models.IntegerField(default=0)
    #historical????????

    def __str__(self):
        return self.name


