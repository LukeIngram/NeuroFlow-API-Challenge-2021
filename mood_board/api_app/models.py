from django.db import models
from django.contrib.auth.models import User
    
class MoodEntry(models.Model): 
    mood_status = models.CharField(max_length=100)
    #date = TODO

    def __str__(self): 
        #---------------------REMOVE ME
        return self.mood_status
