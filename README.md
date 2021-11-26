# NeuroFlow-API-Challenge-2021
Web REST App - Python &amp; Django 

## Contents 
* [General-Info](#general-info)
* [Quickstart](#quickstart)
* [API-Usage](#api-usage)
* [Production-Info](#production-info)

## General-Info
Created & Currently maintained by Luke Ingram.

A Simple backend REST API which serves as a 'mood' entry system for authenticated users.


## Quickstart
To begin, clone this repo...
```
git clone https://github.com/LukeIngram/NeuroFlow-API-Challenge-2021.git
```
Then, Naviagte to [yourpath]/NeuroFlow-API-Challenge-2021, to set and activate a new virtual environment.

##### Note: If you're unfamilair with setting up virual environments, you can follow a this guide: https://docs.python.org/3/library/venv.html



### Installing Necessary Django Packages
```
pip install django 
pip install djangorestframework
```
(See requirements.txt for a full list of requirements)

After Installing all required tools, navigate to the project folder: 
```
cd mood_board/
```
And we're going to create an admin user for our API, so 
we run the following command: 
```
python manage.py createsuperuser
```
Then follow the steps to finish creating your new superuser. 

After we've created out admin, we start the server with the following command. 
```
python manage.py runserver
```
If you wish to add more users, navigate to http://127.0.0.1:8000/admin sign in with your superuser cridentials, and you can add aditional users within that interface.

Now with a running server & and user(s), you should be ready to use this REST API.

## API-Usage 
### Mood List View: 
The first section of the 'mood/' endpoint is located at http://127.0.0.1:8000/api/mood 

If you're not signed in, you'll be met with a 403, & you can use the login button in the top right to autheticate your session. 

If Authenticated, you'll see the "Mood List View" which is a dashboard where users can see all of their mood entries, as well as enter new ones with the POST method. All POSTed mood entries persist in the internal database & are obtianed with the GET method. 

### Mood Entry View: 
Users can view Individual Mood Entries by navigating to http://127.0.0.1:8000/api/mood/[ID] (replacing [ID] with the ID number of the mood entry).

Users can also delete entries in this view if they wish. 

### Mood Board Information View: 
Users can find information about their Mood Board at http://127.0.0.1:8000/api/mood/info 

This report contains important information such as, total number of mood entries, **current streak**, user ID, & username. 

##### **Note: the streaks calculation works in real server time. And if you wish to see it's functionality without waiting several days, the tests which use "mock time" can be found at lines 105-211 of "rest_api/tests.py".**

### System Tests:
This sotware was devloped using the TDD approach. The tests can be found at rest_api/tests.py, & ran with command: 
```
python manage.py test 
```

## Production-Info
As this is an assesment, the API in it's current state, is inadequate for production usage, and if it were to be used, the following changes need to be made:
### Security Changes:  
* The "SECTRET_KEY", while SHA-256, is publicly visible in this REPO, and would typically be hidden within an enviromnent file. 
* While the built-in djnago.auth User model fits well within the scope of this assesment, a custom & more secure user model would be necessary for production use.  
* The "DEBUG" setting would of course be set to False. 

### Technical Changes:
* This API uses an internal databse & was not designed to handle large quantites of users & interal data. In production external database support (AWS? maybe) would be intergrated. 
* Currently this system requires all users to be indivdually added by the admin, which would obvously be illogical in a high traffic system. Rather a form-based login & registration structure should be implimented to midigate this.
* Templates and rudametry font-end support would be nice for a production application 
* The ability to edit or a PATCH method for mood entries would be nice in production, but not essential for this assesment. 
* The structure of this README.md is very unorthadox, in production, a conventonal & formalized documentation will be required. 