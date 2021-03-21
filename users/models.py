from django.db import models
from datetime import datetime
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


# Create your models here.
class User(models.Model):
    #DADES PERSONALS
    id = models.IntegerField
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    birthdate = models.DateField()
    #DADES ESPORTIVES
    activitiesdone = models.IntegerField(default = 0)
    #archivements =
    points = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    objective = models.CharField(max_length=200)
    #interestcategories = #?????
    #DADES FISIQUES
    weight = models.IntegerField()
    height = models.IntegerField()
    imc = models.IntegerField()
    igc = models.IntegerField()
    #historical????????

    def __str__(self):
        return self.name
