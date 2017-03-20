# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-29 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_inspection', '0015_inspector_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=50)),
                ('ccardHolder', models.CharField(max_length=50)),
                ('ccardNumber1', models.CharField(max_length=4)),
                ('ccardNumber2', models.CharField(max_length=4)),
                ('ccardNumber3', models.CharField(max_length=4)),
                ('ccardNumber4', models.CharField(max_length=4)),
                ('ccardExpDateMth', models.CharField(max_length=2)),
                ('ccardExpDateYr', models.CharField(max_length=2)),
                ('ccardSecurity', models.CharField(max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='inspector',
            name='memberStatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='inspector',
            name='subscriptionStatus',
            field=models.BooleanField(default=False),
        ),
    ]