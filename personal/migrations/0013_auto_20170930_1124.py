# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 11:24
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0012_auto_20170930_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankmembership',
            name='acctnbr',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in a number format.', regex='^[1-9]\\d*$')], verbose_name='Account Number'),
        ),
        migrations.AlterUniqueTogether(
            name='personalinfo',
            unique_together=set([('first_name', 'middle_name', 'last_name')]),
        ),
    ]
