# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 11:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0014_auto_20170930_1125'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='addressinfo',
            unique_together=set([('person', 'address_type')]),
        ),
    ]