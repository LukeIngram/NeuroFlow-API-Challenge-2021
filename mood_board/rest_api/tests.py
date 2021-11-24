from django.test import TestCase, client
from django.contrib.auth.models import User
from django.urls import reverse 
from .models import * 
from .views import *

class Mood_Entry_Tests(TestCase): 
    def setUp(self): 
        testUser = User.objects.create_user(username='flynn',password='flynns_super_secret_password')
        testUser.save()
        test_entry = moodEntry.objects.create(id=1,status="Weary...",created_by=testUser)
        test_entry.save()

    def test_mood_entry_has_user_and_satus(self): 
        entry = moodEntry.objects.get(id=1)
        status = f'{entry.status}'
        user = f'{entry.created_by}'

        self.assertEqual(status,'Weary...')
        self.assertEqual(user,'flynn')
    
    def test_get_mood_entry(self): 
        self.client.login(username='flynn', password='flynns_super_secret_password')
        response = self.client.get(reverse('moodBoard:moodEntry',args=[1]))

        self.assertEqual(response.status_code,200) 
        self.assertEqual(response.data['id'],1)
        self.assertEqual(response.data['status'],'Weary...')
    
    def test_get_mood_entry_unauth(self): 
        response = self.client.get(reverse('moodBoard:moodEntry',args=[1]))
        self.assertEqual(response.status_code,403) 
    
    def test_get_unknown_mood_entry(self): 
        self.client.login(username='flynn', password='flynns_super_secret_password')
        response = self.client.get(reverse('moodBoard:moodEntry',args=[2]))
        self.assertEqual(response.status_code,404)

    #TODO POST METHOD (ENTRY CRAEATON) TESTS 

    def test_create_new_entry(self): 
        self.client.login(username='flynn', password='flynns_super_secret_password')
        response = self.client.post(reverse('moodBoard:moodEntry',args=[{"status": "Quite Curious"}]))
        pass #TODO

#TODO USER CREATION & MANAGEMENT TESTS 



#TODO full system tests 
