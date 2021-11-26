from rest_framework import serializers
from .models import * 
from datetime import timedelta
from django.utils.timezone import utc
from django.contrib.auth import get_user_model

class MoodEntrySerializer(serializers.ModelSerializer): 
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta: 
        model = moodEntry
        fields = ('id','status','created_at','created_by')



class MoodBoardSerializer(serializers.ModelSerializer): 
    id = serializers.IntegerField()
    moodBoard = MoodEntrySerializer(many=True,read_only=True)
   
    current_streak = serializers.SerializerMethodField(method_name='has_streak')
    def has_streak(self,user): 
        curr_streak = 1
        entry_dates = list(moodEntry.objects.values('created_at').filter(created_by=user).order_by('created_at'))
        if len(entry_dates) <= 1: 
            return len(entry_dates)
        else: 
            for i in range(len(entry_dates)-1): 
                entry_time_diff = abs(entry_dates[i]['created_at'].date() - entry_dates[i+1]['created_at'].date())
                if entry_time_diff > timedelta(days=1):
                    curr_streak = 1
                elif entry_time_diff.days == 1:  
                    curr_streak += 1
            return curr_streak      
    
    entry_count = serializers.SerializerMethodField(method_name='getEntryCount')
    def getEntryCount(self,user): 
        return moodEntry.objects.filter(created_by=user).count()

    class Meta: 
        model = get_user_model()
        fields = ('id','username','entry_count','current_streak','moodBoard')
        

    
    