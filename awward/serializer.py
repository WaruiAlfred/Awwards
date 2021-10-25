from rest_framework import serializers
from .models import Profile,Projects,Ratings

#Profile serializer class
class ProfileSerializer(serializers.ModelSerializer): 
  class Meta: 
    model = Profile
    fields = '__all__'
    
#Projects serializer class
class ProjectsSerializer(serializers.ModelSerializer): 
  class Meta: 
    model = Projects
    fields = '__all__'
    
#Ratings serializer class
class RatingsSerializer(serializers.ModelSerializer): 
  class Meta: 
    model = Ratings
    fields = '__all__'