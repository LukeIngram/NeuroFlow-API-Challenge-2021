from rest_framework import serializers
from .models import * 
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class MoodEntrySerializer(serializers.ModelSerializer): 
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta: 
        model = moodEntry
        fields = ('id','status','created_at','created_by')

class MoodBoardSerializer(serializers.ModelSerializer): 
    id = serializers.IntegerField(source='id')
    moodBoard = MoodEntrySerializer(many=True,read_only=True)
   
   
    streak = serializers.SerializerMethodField(method_name='has_streak')
    def has_streak(self,user): 
        #TODO impliment streak calculation 
        pass 

    #TODO get last streak 

    
    entry_count = serializers.SerializerMethodField(method_name='getEntryCount')
    def getEntryCount(self): 
        return len(moodEntry.objects.filter(user=self.context['request'].user))

    

    class Meta: 
        model = get_user_model()
        fields = {'id','username','entry_count','last_entry_date','current_streak','mood'}
        

    
    