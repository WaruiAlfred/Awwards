from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

#Projects model
class Projects(models.Model): 
  project_owner = models.ForeignKey(User,on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  description = models.TextField()
  screenshot = CloudinaryField('project')
  live_link = models.URLField(max_length=100)
  date_added = models.DateField(auto_now_add=True)
  
  def __str__(self):
    return self.name 
  
  