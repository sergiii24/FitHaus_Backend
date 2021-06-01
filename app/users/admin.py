from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(ExternUser)
admin.site.register(NormalUser)
