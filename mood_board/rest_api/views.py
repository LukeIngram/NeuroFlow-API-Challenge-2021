from django.shortcuts import render,redirect
from rest_framework import generics, viewsets 
from .models import * 
from .serializers import * 

class MoodEntryView(generics.ListAPIView): 
    def get_queryset(self):
        return moodEntry.ojects.filter(user=self.request.user)
    queryset = moodEntry.objects.all()
    serializer = MoodEntrySerializer 

#TODO MoodBoard View 


