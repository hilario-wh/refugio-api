# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-05-19 22:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atributo',
            name='uuid',
        ),
        migrations.RemoveField(
            model_name='atributovalor',
            name='uuid',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='uuid',
        ),
    ]