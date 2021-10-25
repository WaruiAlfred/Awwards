from django.urls import path,include
from . import views
from rest_framework import routers

#API routes
router = routers.DefaultRouter()
router.register('profiles',views.ProfileView)
router.register('projects',views.ProjectsView)
router.register('projects_ratings',views.RatingsView)

#awward app urls
urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('profile/update/',views.update_profile,name='profileUpdate'),
    path('post_project/',views.post_project,name='post_project'),
    path('search/project/',views.search_project,name='search_project'),
    path('rate_project/<int:project_id>',views.rate_project,name='rate'),
    path('details/project/<int:project_id>',views.project_details,name='project_details'),
    
    path('api/',include(router.urls)),
]
