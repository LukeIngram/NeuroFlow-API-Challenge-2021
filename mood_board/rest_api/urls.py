from django.urls import path
from .views import * 


urlpatterns = [
    path(r'mood/<int:pk>',MoodEntryView.as_view(),name='moodEntry'),
    path(r'mood/info',MoodBoardView.as_view({'get':'list'}),name='moodBoard'),
    path(r'mood/',MoodListView.as_view(),name='moodList'),
]

