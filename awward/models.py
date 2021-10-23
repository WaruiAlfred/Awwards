from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

#Projects model
class Projects(models.Model): 
  project_owner = models.ForeignKey(User,on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=400)
  screenshot = CloudinaryField('screenshot')
  live_link = models.URLField(max_length=100)
  date_added = models.DateField(auto_now_add=True)
  
  def __str__(self):
    return self.name 
  
#Profile model
class Profile(models.Model): 
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  bio = models.TextField(max_length=400)
  country = models.CharField(max_length=30)
  phone_number = models.CharField(max_length=10)
  picture = CloudinaryField('profile')
  
  def save_profile(self): 
    '''Funtion to save a profile object'''
    self.save()
  
  def __str__(self):
    return self.user.username
  