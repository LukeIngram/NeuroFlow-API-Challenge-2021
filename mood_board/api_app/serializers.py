from rest_framework import serializers
from .models import MoodEntry 

class MoodSerializer(serializers.ModelSerializer): 
    mood_status = serializers.CharField(max_length=100)

    class Meta: 
        model = MoodEntry
        fields =('__all__')