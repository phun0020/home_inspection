# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-29 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_inspection', '0014_remove_inspector_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspector',
            name='password',
            field=models.CharField(default='password', max_length=25),
            preserve_default=False,
        ),
    ]