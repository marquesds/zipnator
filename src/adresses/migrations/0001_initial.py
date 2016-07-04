# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 23:55
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=300, verbose_name='Street')),
                ('district', models.CharField(max_length=200, verbose_name='District')),
                ('city', models.CharField(max_length=200, verbose_name='City')),
                ('state', models.CharField(max_length=200, verbose_name='State')),
                ('zipcode', models.CharField(max_length=9, unique=True, validators=[django.core.validators.RegexValidator(message='Invalid zipcode', regex=re.compile('^\\d{5}-?\\d{3}', 32))], verbose_name='Zipcode')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Adresses',
            },
        ),
    ]
