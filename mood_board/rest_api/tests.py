from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,timedelta
from unittest import mock
from .models import * 
from .views import *

class Mood_Entry_Tests(TestCase): 
    def setUp(self): 
        testUser = User.objects.create_user(username='flynn',password='flynns_super_secret_password')
        testUser.save()
        test_entry = moodEntry.objects.create(id=1,status="Weary...",created_by=testUser)
        test_entry.save()

    def test_mood_entry_has_user_and_status(self): 
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

    def test_get_mood_list_unauth(self):
        response = self.client.get(reverse('moodBoard:moodList'))
        self.assertEqual(response.status_code,403)
    
    def test_list_only_contains_logged_in_user_moods(self): 
        testUser = User.objects.create_user(username='beboop',password='secret_wordz')
        testUser.save()
        test_entry = moodEntry.objects.create(id=3,status="lonley...",created_by=testUser)
        test_entry.save()
        self.client.login(username='beboop',password='secret_wordz')
        response = self.client.get(reverse('moodBoard:moodList'))
        self.assertEqual(len(response.data),1)
        self.assertEqual(response.data[0]['id'],3)
        self.assertEqual(response.data[0]['status'],'lonley...')

    def test_create_new_entry(self): 
        self.client.login(username='flynn', password='flynns_super_secret_password')
        response = self.client.post(reverse('moodBoard:moodList'),{'status':'happy!!'})
        self.assertEqual(response.data['id'],3)
        self.assertEqual(response.data['status'],'happy!!')

    def test_create_new_mood_entry_unauth(self):
        response = self.client.post(reverse('moodBoard:moodList'),{'status':'happy!!'})
        self.assertEqual(response.status_code,403)
        
    def test_create_new_mood_entry_invalid_request(self): 
        self.client.login(username='flynn', password='flynns_super_secret_password')
        response = self.client.post(reverse('moodBoard:moodList'),{'created_at':'11/23/2021'})
        self.assertEqual(response.status_code,400)
        

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
        self.assertEqual(response.data[0]['current_streak'],1)   


    def test_entry_count_unauth(self): 
        response = self.client.get(reverse('moodBoard:moodBoard'))
        self.assertEqual(response.status_code,403)

class Entry_Streak_Tests(TestCase): 
    def setUp(self):
        testUser = User.objects.create_user(username='flynn',password='flynns_super_secret_password')
        testUser.save()

    def test_user_with_no_entries_has_zero_streak(self):
        self.client.login(username='flynn', password='flynns_super_secret_password')
        response = self.client.get(reverse('moodBoard:moodBoard'))
        self.assertEqual(response.data[0]['current_streak'],0)
    
    def test_user_with_one_entry_as_one_day_streak(self): 
        self.client.login(username='flynn', password='flynns_super_secret_password')
        test_entry = moodEntry.objects.create(id=1,status="Weary...",created_by=User.objects.get(username='flynn'))
        test_entry.save()
        response = self.client.get(reverse('moodBoard:moodBoard'))
        self.assertEqual(response.data[0]['current_streak'],1)
    
    def test_user_has_3_day_streak(self): 
        self.client.login(username='flynn', password='flynns_super_secret_password')
        for i in range(1,4): 
            mock_time = datetime.utcnow().replace(tzinfo=utc) + timedelta(days=(i-1))
            with mock.patch('django.utils.timezone.now') as mock_now:
                mock_now.return_value = mock_time
                test_entry = moodEntry.objects.create(id=i,status="test_mood%s"%(i),created_by=User.objects.get(username='flynn'))
                test_entry.save()
        response = self.client.get(reverse('moodBoard:moodBoard'))
        self.assertEqual(response.data[0]['current_streak'],3)
    
    def test_user_has_20_day_streak(self): 
        self.client.login(username='flynn', password='flynns_super_secret_password')
        for i in range(1,21): 
            mock_time = datetime.utcnow().replace(tzinfo=utc) + timedelta(days=(i-1))
            with mock.patch('django.utils.timezone.now') as mock_now:
                mock_now.return_value = mock_time
                test_entry = moodEntry.objects.create(id=i,status="test_mood%s"%(i),created_by=User.objects.get(username='flynn'))
                test_entry.save()
        response = self.client.get(reverse('moodBoard:moodBoard'))
        self.assertEqual(response.data[0]['current_streak'],20)
    
    def test_user_breaks_streak(self): 
        self.client.login(username='flynn', password='flynns_super_secret_password')
        for i in range(1,7): 
            if i == 5:
                continue
            else: 
                time_diff = timedelta(days=(i-1))
            mock_time = datetime.utcnow().replace(tzinfo=utc) + time_diff
            with mock.patch('django.utils.timezone.now') as mock_now:
                mock_now.return_value = mock_time
                test_entry = moodEntry.objects.create(id=i,status="test_mood%s"%(i),created_by=User.objects.get(username='flynn'))
                test_entry.save()
        response = self.client.get(reverse('moodBoard:moodBoard'))
        self.assertEqual(response.data[0]['current_streak'],1)
    
    def test_user_breaks_streak_in_middle(self): 
        self.client.login(username='flynn', password='flynns_super_secret_password')
        for i in range(1,11): 
            if i == 3:
                continue
            else: 
                time_diff = timedelta(days=(i-1))
            mock_time = datetime.utcnow().replace(tzinfo=utc) + time_diff
            with mock.patch('django.utils.timezone.now') as mock_now:
                mock_now.return_value = mock_time
                test_entry = moodEntry.objects.create(id=i,status="test_mood%s"%(i),created_by=User.objects.get(username='flynn'))
                test_entry.save()
        response = self.client.get(reverse('moodBoard:moodBoard'))
        self.assertEqual(response.data[0]['current_streak'],7)
    
    def test_user_deleting_entry_breaks_streak(self): 
        self.client.login(username='flynn', password='flynns_super_secret_password')
        for i in range(1,11): 
            mock_time = datetime.utcnow().replace(tzinfo=utc) + timedelta(days=(i-1))
            with mock.patch('django.utils.timezone.now') as mock_now:
                mock_now.return_value = mock_time
                test_entry = moodEntry.objects.create(id=i,status="test_mood%s"%(i),created_by=User.objects.get(username='flynn'))
                test_entry.save()
        r1 = self.client.get(reverse('moodBoard:moodBoard'))
        self.assertEqual(r1.data[0]['current_streak'],10)
        self.client.delete(reverse('moodBoard:moodEntry',args=[5]))
        r2 = self.client.get(reverse('moodBoard:moodBoard'))
        self.assertEqual(r2.data[0]['current_streak'],5)