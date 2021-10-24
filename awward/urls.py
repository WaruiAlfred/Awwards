from django.urls import path
from . import views

#awward app urls
urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('profile/update/',views.update_profile,name='profileUpdate'),
    path('search/project/',views.search_project,name='search_project'),
    path('rate_project/<int:project_id>',views.rate_project,name='rate'),
]
