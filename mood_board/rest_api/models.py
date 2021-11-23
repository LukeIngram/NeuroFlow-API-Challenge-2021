from django.db import models


class moodEntry(models.Model): 
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    #created_by = 



