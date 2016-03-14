# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-03 17:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=120)),
                ('category', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=150)),
                ('area', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=5)),
                ('phone', models.CharField(default=None, max_length=20, null=True)),
                ('notes', models.TextField(default=None, max_length=500, null=True)),
                ('website', models.URLField(default=None, max_length=120, null=True)),
                ('price', models.CharField(default=None, max_length=5, null=True)),
                ('parking', models.CharField(default=None, max_length=20, null=True)),
                ('maps', models.URLField(default=None, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('count', models.IntegerField(default=0)),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]