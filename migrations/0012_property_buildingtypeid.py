# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-29 17:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_inspection', '0011_auto_20170127_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='buildingTypeId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home_inspection.BuildingType'),
        ),
    ]
