from django.contrib.auth import views as auth_views
from django.db.models import base
from django.urls import path,include
from .views import * 

#TODO Configure routing for viewset (MoodBoard) & paths for generics 


urlpatterns = [
    path(r'mood/<int:pk>',MoodEntryView.as_view(),name='moodEntry'),
    path(r'mood/info',MoodBoardView.as_view({'get':'list'}),name='moodBoard'),
    path(r'mood/list-view',MoodListView.as_view(),name='moodList'),
    #path(r'mood/',MoodEntryView.post()),
    #TODO add dedicated create urL???
]
