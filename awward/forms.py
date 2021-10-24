from django import forms
from .models import Profile,Projects,Ratings,RATE_CHOICES
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
    fields = ['name','description','main_technology_used','live_link','screenshot']
    
#Rating form
class ProjectRatingForm(forms.ModelForm): 
  review = forms.CharField(widget=forms.Textarea(),required=False)
  design_rate = forms.ChoiceField(choices=RATE_CHOICES,widget=forms.Select(),required=True)
  usability_rate = forms.ChoiceField(choices=RATE_CHOICES,widget=forms.Select(),required=True)
  content_rate = forms.ChoiceField(choices=RATE_CHOICES,widget=forms.Select(),required=True)
 
  class Meta: 
    model = Ratings
    fields = ('design_rate','usability_rate','content_rate','review') 