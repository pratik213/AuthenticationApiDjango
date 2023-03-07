from django.contrib import admin
from . models import RegisterUser,UserProfile

# Register your models here.
admin.site.register(RegisterUser)
admin.site.register(UserProfile)