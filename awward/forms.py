from django import forms
from .models import Profile,Projects
from django.contrib.auth.models import User

#Profile form
class ProfileUpdateForm(forms.ModelForm): 
  class Meta: 
    model = Profile
    fields = ['bio','country','phone_number','picture']
    
#User update form
class UserUpdateForm(forms.ModelForm): 
  class Meta: 
    model = User
    fields = ['username','email']
    
#Posting project form
class ProjectAddForm(forms.ModelForm): 
  class Meta: 
    model = Projects
    fields = ['name','description','live_link','screenshot']