# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-25 15:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dates', '0002_auto_20160325_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dates',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]