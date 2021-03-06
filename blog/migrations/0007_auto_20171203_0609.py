# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_travel_groups'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Travel_groups',
            new_name='Travel_group',
        ),
        migrations.AlterModelOptions(
            name='travel_group',
            options={'ordering': ('group_name',)},
        ),
        migrations.AddField(
            model_name='profile',
            name='travel_groups',
            field=models.ManyToManyField(to='blog.Travel_group'),
        ),
    ]
