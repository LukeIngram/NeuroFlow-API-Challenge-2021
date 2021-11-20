# api_app urls.py
from django.urls import path
from .views import MoodView

urlpatterns = [
    path('mood/', MoodView.as_view()),
    path('mood/<int:id>', MoodView.as_view())
]
