# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 01:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='size_chart',
            old_name='ID',
            new_name='Length_ID',
        ),
    ]