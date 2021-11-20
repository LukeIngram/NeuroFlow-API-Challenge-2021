# api_app urls.py
from django.urls import include, path
from .views import ListMoodEntryView, MoodView

urlpatterns = [
    path('', ListMoodEntryView.as_view()),
    path('mood/', MoodView.as_view(),name="Mood Entries"),
    path('mood/<int:id>', MoodView.as_view()),
]
