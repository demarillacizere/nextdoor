# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-04 21:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nextdoor', '0003_auto_20210204_0840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighborhood',
            old_name='occupants',
            new_name='occupants_count',
        ),
    ]
