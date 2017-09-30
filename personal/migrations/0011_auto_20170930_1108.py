# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 11:08
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0010_auto_20170929_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankinfo',
            name='phone_nbr',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Branch Phone Number'),
        ),
        migrations.AlterField(
            model_name='bankmembership',
            name='acctnbr',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '999999999'. Up to 15 digits allowed.", regex='^\\1?\\d{9,15}$')], verbose_name='Account Number'),
        ),
    ]
