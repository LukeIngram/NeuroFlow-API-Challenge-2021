from rest_framework import serializers
from .models import * 

#TODO make User serializer 


#class MoodBoardStabilizeer(serializers.ModelSerializer): 


class MoodEntrySerializer(serializers.ModelSerializer): 
    mood_status = serializers.CharField(max_length=100)

    class Meta: 
        model = MoodEntry
        fields =('__all__')
    