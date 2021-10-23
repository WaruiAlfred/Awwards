from django.urls import path
from . import views

#awward app urls
urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('profile/update/',views.update_profile,name='profileUpdate'),
    # path('projects/',views.project,name='projects'),
]
