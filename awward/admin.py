from django.contrib import admin
from .models import Projects,Profile,Ratings

#Registering models
admin.site.register(Projects)
admin.site.register(Profile)
admin.site.register(Ratings)