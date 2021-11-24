from django import test
from django.http import response
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

    def test_remove_mood_entry(self): 
        self.client.login(username='flynn', password='flynns_super_secret_password')
        response = self.client.delete(reverse('moodBoard:moodEntry',args=[1]))
        self.assertEqual(response.status_code,200)
        self.assertEqual(self.client.get(reverse('moodBoard:moodEntry',args=[1])).status_code,404)
    
    def test_remove_unknown_mood_entry(self): 
        self.client.login(username='flynn', password='flynns_super_secret_password')
        response = self.client.delete(reverse('moodBoard:moodEntry',args=[2]))
        self.assertEqual(response.status_code,404)
        self.assertEqual(self.client.get(reverse('moodBoard:moodEntry',args=[1])).status_code,200)
    
    def test_remove_mood_entry_unauth(self): 
        response = self.client.delete(reverse('moodBoard:moodEntry',args=[1]))
        self.assertEqual(response.status_code,403) 

    '''
    def test_create_new_entry(self): 
        self.client.login(username='flynn', password='flynns_super_secret_password')
        response = self.client.post(reverse('moodBoard:moodEntry'))
    '''

#TODO MoodList TESTS
class Mood_List_Tests(TestCase):
    def setUp(self): 
        testUser = User.objects.create_user(username='flynn',password='flynns_super_secret_password')
        testUser.save()
        test_entry1 = moodEntry.objects.create(id=1,status="Weary...",created_by=testUser)
        test_entry2 = moodEntry.objects.create(id=2,status="excited!!!!",created_by=testUser)
        test_entry1.save()
        test_entry2.save()

    def test_get_mood_list(self): 
        self.client.login(username='flynn', password='flynns_super_secret_password')
        response = self.client.get(reverse('moodBoard:moodList'))
        self.assertEqual(len(response.data),2)
        self.assertEqual(response.data[0]['id'],1)
        self.assertEqual(response.data[0]['status'],'Weary...')
        self.assertEqual(response.data[1]['id'],2)
        self.assertEqual(response.data[1]['status'],'excited!!!!')

#TODO MOOD BOARD TESTS (STREAKS & ENTRY CREATION)
class Mood_Board_Tests(TestCase): 

    def setUp(self): 
        testUser1 = User.objects.create_user(username='flynn',password='flynns_super_secret_password')
        testUser2 = User.objects.create_user(username='beboop',password='secret_wordz')
        testUser1.save()
        testUser2.save()
        test_entry1 = moodEntry.objects.create(id=1,status="Weary...",created_by=testUser1)
        test_entry2 = moodEntry.objects.create(id=2,status="suspicious",created_by=testUser2)
        test_entry1.save()
        test_entry2.save()
    
    def test_entry_count(self): 
        self.client.login(username='flynn', password='flynns_super_secret_password')
        response = self.client.get(reverse('moodBoard:moodBoard'))
        self.assertEqual(response.data[0]['id'],1)
        self.assertEqual(response.data[0]['username'],'flynn')
        self.assertEqual(response.data[0]['entry_count'],1)
        #TODO ASSERT CURRENT STREEAK    


    def test_entry_count_unauth(self): 
        response = self.client.get(reverse('moodBoard:moodBoard'))
        self.assertEqual(response.status_code,403)


        



#TODO USER CREATION & MANAGEMENT TESTS 



#TODO full system tests 
