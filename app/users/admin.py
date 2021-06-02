from django.contrib import admin

# Register your models here.
from users.models import User, ExternUser, NormalUser

admin.site.register(User)
admin.site.register(ExternUser)
admin.site.register(NormalUser)
