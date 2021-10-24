from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

#Projects model
class Projects(models.Model): 
  project_owner = models.ForeignKey(User,on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=400)
  main_technology_used = models.CharField(max_length=30,null=True)
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

#Rate/Review model

RATE_CHOICES = [
  (1, '1 - Unlikeable'),
  (2, '2 - Horrible'),
  (3, '3 - Hmmmm'),
  (4, '4 - Bad'),
  (5, '5 - Fine'),
  (6, '6 - Good'),
  (7, '7 - Very Good'),
  (8, '8 - Likeable'),
  (9, '9 - Perfect'),
  (10, '10 - Awesome'),
]

class Ratings(models.Model): 
  user = models.ForeignKey(User,on_delete=models.CASCADE)  
  project = models.ForeignKey(Projects,on_delete=models.CASCADE)  
  design_rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
  usability_rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
  content_rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
  review = models.TextField(max_length=1000,blank=True)
  date = models.DateField(auto_now_add=True)
  
  def __str__(self):
    return self.project.name