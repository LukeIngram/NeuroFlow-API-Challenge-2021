from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class MoodBoard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mood_board", null=True,default=1)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MoodEntry(models.Model): 
    mood_status = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self): 
        #---------------------REMOVE ME
        return self.mood_status
