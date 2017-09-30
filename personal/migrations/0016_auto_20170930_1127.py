# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 11:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0015_auto_20170930_1126'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bankinfo',
            unique_together=set([('name', 'branch')]),
        ),
        migrations.AlterUniqueTogether(
            name='bankmembership',
            unique_together=set([('person', 'bank', 'acct_type', 'acctnbr')]),
        ),
    ]
