# Generated by Django 3.2.9 on 2021-11-18 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_auto_20211118_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='state',
        ),
    ]
