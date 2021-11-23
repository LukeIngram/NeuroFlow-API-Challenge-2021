from django.contrib.auth import views as auth_views
from django.db.models import base
from rest_framework import routers
from django.urls import path,include
from .views import * 

#TODO Configure routing for viewset (MoodBoard) & paths for generics 
# 

router = routers.DefaultRouter()
#router.register([TODO]) 

urlpatterns = [
    #TODO add path for generics here 
]

urlpatterns += router.urls