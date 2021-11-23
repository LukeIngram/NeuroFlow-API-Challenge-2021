from django.test import TestCase
from django.contrib.auth.models import User
from .models import * 

class Mood_Board_Tests(TestCase): 
    def setUp(self): 
        testUser = User.objects.create_user(username='flynn',password='flynns_super_secret_password')
        testUser.save()
        test_entry = moodEntry.objects.create(status="Weary...",created_by=testUser)
        test_entry.save()


