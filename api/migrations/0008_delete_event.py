# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 06:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_event_run'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
    ]
