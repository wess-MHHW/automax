# Generated by Django 5.1.1 on 2024-09-07 14:26

import localflavor.us.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='zid_code',
        ),
        migrations.AddField(
            model_name='location',
            name='zid_code',
            field=localflavor.us.models.USZipCodeField(blank=True, max_length=10),
        ),
    ]
