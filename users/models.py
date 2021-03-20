from django.db import models


# Create your models here.
class User(models.Model):
    #DADES PERSONALS
    id = models.IntegerField
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    birthdate = models.DateField
    #DADES ESPORTIVES
    activitiesdone = models.IntegerField
    #archivements =
    points = models.IntegerField
    level = models.IntegerField
    objective = models.CharField(max_length=200)
    #interestCategories = #?????
    #DADES FISIQUES
    weight = models.IntegerField
    height = models.IntegerField
    imc = models.IntegerField
    igc = models.IntegerField
    #historical????????

    def __str__(self):
        return self.name
