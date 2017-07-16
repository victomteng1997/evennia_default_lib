# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0007_auto_20150403_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scriptdb',
            name='db_attributes',
            field=models.ManyToManyField(help_text=b'attributes on this object. An attribute can hold any pickle-able python object (see docs for special cases).', to='typeclasses.Attribute'),
        ),
        migrations.AlterField(
            model_name='scriptdb',
            name='db_tags',
            field=models.ManyToManyField(help_text=b'tags on this object. Tags are simple string markers to identify, group and alias objects.', to='typeclasses.Tag'),
        ),
    ]