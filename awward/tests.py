from django.test import TestCase
from .models import Profile,Projects,Ratings
from django.contrib.auth.models import User

#Projects Test Class
class ProjectsTestClass(TestCase): 
  def setUp(self):
    '''Function that runs before other functions'''
    self.new_user = User(username="sanzo",email="sanz@gmail.com",password="ssup123")
    self.new_user.save()
    self.movie = Projects(project_owner=self.new_user,name="Merlin",
                          description="For lovers of magic",
                          main_technology_used='Django',
                          screenshot='screenshot/img.jpg',
                          live_link='https://github.io/merlin')
  
  def tearDown(self):
    User.objects.all().delete()
    Projects.objects.all().delete()
  
  def test_instance(self): 
    '''Test function to confirm that the object actually exists after creation'''
    self.assertTrue(isinstance(self.movie,Projects))
  
  def test_save(self):  
    '''Function testing save method'''
    self.movie.save_project()
    projects = Projects.objects.all()
    self.assertTrue(len(projects) > 0)
    
#Ratings Test Class
class RatingsTestClass(TestCase): 
  def setUp(self):
    '''Function that runs before other functions'''
    self.new_user = User(username="sanzo",email="sanz@gmail.com",password="ssup123")
    self.new_user.save()
    
    self.movie = Projects(project_owner=self.new_user,name="Merlin",
                          description="For lovers of magic",
                          main_technology_used='Django',
                          screenshot='screenshot/img.jpg',
                          live_link='https://github.io/merlin')
    self.movie.save_project()
    
    self.rating = Ratings(user=self.new_user,
                          project=self.movie,
                          design_rate=7,
                          usability_rate=8,
                          content_rate=6)
  
  def tearDown(self):
    User.objects.all().delete()
    Projects.objects.all().delete()
    Ratings.objects.all().delete()
  
  def test_instance(self): 
    '''Test function to confirm that the object actually exists after creation'''
    self.assertTrue(isinstance(self.rating,Ratings))
  
  def test_save(self):  
    '''Function testing save method'''
    self.rating.save_rating()
    ratings = Ratings.objects.all()
    self.assertTrue(len(ratings) > 0)
    
#Profile Test Class
class ProfileTestClass(TestCase): 
  def setUp(self):
    '''Function that runs before other functions'''
    self.new_user = User(username="sanzo",email="sanz@gmail.com",password="ssup123")
    self.new_user.save()
    self.user_profile = Profile(user=self.new_user,
                                bio='I love gaming',
                                country='Kenya',
                                phone_number='0712345678',
                                picture='profile/avatar.jpg')
  
  def tearDown(self):
    User.objects.all().delete()
    Profile.objects.all().delete()
  
  def test_instance(self): 
    '''Test function to confirm that the object actually exists after creation'''
    self.assertTrue(isinstance(self.user_profile,Profile))
  
  def test_save(self):  
    '''Function testing save method'''
    self.user_profile.save_profile()
    profiles = Profile.objects.all()
    self.assertTrue(len(profiles) > 0)