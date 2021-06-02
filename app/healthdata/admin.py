from django.contrib import admin

# Register your models here.
from healthdata.models import HealthData

admin.site.register(HealthData)
