# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 01:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userDashboard', '0002_user_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='description',
        ),
    ]
