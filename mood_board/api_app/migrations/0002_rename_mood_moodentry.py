# Generated by Django 3.2.9 on 2021-11-20 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mood',
            new_name='MoodEntry',
        ),
    ]