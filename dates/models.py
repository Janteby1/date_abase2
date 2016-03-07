from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone #make sure to set the timezone 
from django.core.exceptions import ValidationError


CATEGORIES = (  
    ('ACT1', 'Activity (Acrobatic)'),
    ('ACT2', 'Activity (Arcade)'),
    ('ACT3', 'Activity (Archery)'),
    ('ACT4', 'Activity (Bar)'),
    ('ACT5', 'Activity (Billiards)'),
    ('ACT6', 'Activity (Boat Rental)'),
    ('ACT7', 'Activity (Boat)'),
    ('ACT8', 'Activity (Bowling)'),
    ('ACT9', 'Activity (Bukket List)'),
    ('ACT10', 'Activity (Chill)'),
    ('ACT11', 'Activity (Experience)'),
    ('ACT12', 'Activity (Mini Golf)'),
    ('ACT13', 'Activity (Horseback Riding)'),
    ('ACT14', 'Activity (Ice Skating)'),
    ('ACT15', 'Activity (Karaoke)'),
    ('ACT16', 'Activity (Go Karting)'),
    ('ACT17', 'Activity (Movies)'),
    ('ACT18', 'Activity (Musuem)'),
    ('ACT19', 'Activity (Painting)'),
    ('ACT20', 'Activity (Park)'),
    ('ACT21', 'Activity (Play)'),
    ('ACT22', 'Activity (Zoo)'),

    ('AMU', 'Amusement Park'),
    ('DES', 'Dessert (D)'),
    ('DES_P', 'Dessert (P)'),
    ('DIN_D', 'Dinner (D)'),
    ('DIN_Deal', 'Dinner (Deal)'),
    ('DIN_M', 'Dinner (M)'),
    ('LUN', 'Lunch (D)'),
    ('STA', 'Stadium'),
    ('WEB', 'Website'),
    )

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

class Dates(models.Model):
    place = models.CharField (max_length=120)
    category = models.CharField (max_length=80, choices=CATEGORIES)
    address = models.CharField (max_length=150)
    area = models.CharField (max_length=30)
    state = models.CharField (max_length=5)
    phone = models.CharField (max_length=20, null = True, default = None,)
    notes = models.TextField (max_length=500, null = True, default = None,)
    website = models.URLField(max_length=120, null = True, default = None,) 
    # website might give us some issues when we try to seed the db
    price = models.CharField (max_length=5, null = True, default = None,)
    parking = models.CharField (max_length=20, null = True, default = None,)
    maps = models.URLField (max_length=200, null = True, default = None,)
    created_at = models.DateTimeField(default = timezone.now, editable=False)
    count = models.IntegerField(default = 0)
    # user = models.ForeignKey(User, null = True, default = None)


    def save(self, *args, **kwargs):
        # self.full_clean()
        super(Dates, self).save(*args, **kwargs)



