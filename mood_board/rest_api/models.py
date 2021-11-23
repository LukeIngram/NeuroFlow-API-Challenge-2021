from django.db import models
from django.contrib.auth.models import User


class moodEntry(models.Model): 
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self): 
        self.status




