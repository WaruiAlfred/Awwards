from django import forms
from django.forms import fields
from .models import Profile
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