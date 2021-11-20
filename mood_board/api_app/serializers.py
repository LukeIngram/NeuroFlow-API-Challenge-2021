from rest_framework import serializers
from .models import * 

#TODO make User serializer 


#class MoodBoardSerializer(serializers.ModelSerializer): 


class MoodEntrySerializer(serializers.ModelSerializer): 
    mood_status = serializers.CharField(max_length=100)
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta: 
        model = MoodEntry
        fields =('__all__')
    