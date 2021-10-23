from django.contrib import admin
from .models import Projects,Profile

#Registering models
admin.site.register(Projects)
admin.site.register(Profile)