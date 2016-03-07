# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-04 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dates', '0002_auto_20160304_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dates',
            name='category',
            field=models.CharField(choices=[('ACT1', 'Activity (Acrobatic)'), ('ACT2', 'Activity (Arcade)'), ('ACT3', 'Activity (Archery)'), ('ACT4', 'Activity (Bar)'), ('ACT5', 'Activity (Billiards)'), ('ACT6', 'Activity (Boat Rental)'), ('ACT7', 'Activity (Boat)'), ('ACT8', 'Activity (Bowling)'), ('ACT9', 'Activity (Bukket List)'), ('ACT10', 'Activity (Chill)'), ('ACT11', 'Activity (Experience)'), ('ACT12', 'Activity (Mini Golf)'), ('ACT13', 'Activity (Horseback Riding)'), ('ACT14', 'Activity (Ice Skating)'), ('ACT15', 'Activity (Karaoke)'), ('ACT16', 'Activity (Go Karting)'), ('ACT17', 'Activity (Movies)'), ('ACT18', 'Activity (Musuem)'), ('ACT19', 'Activity (Painting)'), ('ACT20', 'Activity (Park)'), ('ACT21', 'Activity (Play)'), ('ACT22', 'Activity (Zoo)'), ('AMU', 'Amusement Park'), ('DES', 'Dessert (D)'), ('DES_P', 'Dessert (P)'), ('DIN_D', 'Dinner (D)'), ('DIN_Deal', 'Dinner (Deal)'), ('DIN_M', 'Dinner (M)'), ('LUN', 'Lunch (D)'), ('STA', 'Stadium'), ('WEB', 'Website')], max_length=80),
        ),
    ]
