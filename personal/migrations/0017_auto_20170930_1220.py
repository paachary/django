# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0016_auto_20170930_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankmembership',
            name='acct_type',
            field=models.CharField(choices=[('SB', 'Savings Bank Account'), ('FD', 'Fixed Deposit'), ('RD', 'Recurring Deposit')], default='SB', max_length=2, verbose_name='Account Type'),
        ),
    ]
