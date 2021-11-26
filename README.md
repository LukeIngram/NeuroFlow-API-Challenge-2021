# NeuroFlow-API-Challenge-2021
Web REST App - Python &amp; Django 

## Contents 
* [General-Info](#general-info)
* [Quickstart](#quickstart)
* [API-Usage](#api-usage)
* [Production-Info](#production-info)

## General-Info
NOTE: THE API-USAGE SECTION IS CRITICAL TO UNDERSTANDING THIS API, QUCIKSTART GUIDE MAYBE SKIPPED IF FAMILAIR WITH DJNAGO, BUT PLEASE READ THE API-USAGE SECTION.

Created & currently maintained by Luke Ingram

Simple backend REST API which serves as a 'mood' entry system for authenticated users.


## Quickstart
To begin, clone this repo...
```
$ git clone https://github.com/LukeIngram/NeuroFlow-API-Challenge-2021.git
```
Then, Naviagte to [yourpath]/NeuroFlow-API-Challenge-2021, and set/activate up a new virtual environment.

If you're unfamilair with setting up virual environments, you can follow a this guide: https://docs.python.org/3/library/venv.html



### Installing Necessary Djnago Packages
```
$ pip install django 
$ pip install djangorestframework
```
(See requirements.txt for a full list of requirements)

After Installing all required tools, navigate to the project folder: 
```
$ cd mood_board/
```
And we're going to create an admin user for our API, so 
we run the following command: 
```
python manage.py createsuperuser
```
Then follow the steps to finish creating your new superuser. 

After we've created out admin, we start the server with the following command. 
```
$ python manage.py runserver
```
If you wish to add more users, navigate to http://127.0.0.1:8000/admin sign in with your superuser cridentials, and you can add aditional users within that interface.

Now with a running server & and user(s), you should be ready to use this REST API.

## API-Usage 

### Mood List View: 
The first section of the 'mood/' endpoint is located at http://127.0.0.1:8000/api/mood 

If you're not signed in, you'll be met with a 403, & you can use the login button in the top right to autheticate your session. 

If Authenticated, you'll see the "Mood List View" which is a dashboard where users can see all of their mood entries, as well as post new ones with the POST method. All POSTed info persists & is obtianed with the GET method. 

### Mood Entry View: 
Users can view Individual Mood Entries by navigating to http://127.0.0.1:8000/api/mood/[ID] (replacing [ID] with the ID number of the mood entry).

### Mood Board Information View: 
Users can find information about their Mood Board at http://127.0.0.1:8000/api/mood/info 

This report contains important information such as, total number of mood entries, **current streak**, user ID, & username. 

### System Tests
This sotware was devloped with a TDD model, & the tests can be found at rest_api/tests.py, and ran with command: 
```
$ python manage.py test 
```

## Production-Info
