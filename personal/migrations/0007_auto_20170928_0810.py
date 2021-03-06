# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 08:10
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0006_auto_20170925_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phoneinfo',
            name='phone_nbr',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1+\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='phoneinfo',
            name='phone_type',
            field=models.CharField(choices=[('R', 'Residence'), ('O', 'Office'), ('M', 'Mobile')], default='R', max_length=1),
        ),
    ]
