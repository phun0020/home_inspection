# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 20:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_inspection', '0007_component_faultphoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='faultPhoto',
        ),
    ]
