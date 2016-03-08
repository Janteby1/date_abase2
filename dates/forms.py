from django import forms
from .models import UserProfile, Dates
from django.contrib.auth.models import User


CATEGORIES = (  
    ('ACT1', 'Activity (Acrobatic)'),
    ('ACT2', 'Activity (Arcade)'),
    ('ACT3', 'Activity (Archery)'),
    ('ACT4', 'Activity (Bar)'),
    ('ACT5', 'Activity (Billiards)'),
    ('ACT6', 'Activity (Boat Rental)'),
    ('ACT7', 'Activity (Boat)'),
    ('ACT8', 'Activity (Bowling)'),
    ('ACT9', 'Activity (Bucket List)'),
    ('ACT10', 'Activity (Chill)'),
    ('ACT11', 'Activity (Experience)'),
    ('ACT12', 'Activity (Go Karting)'),
    ('ACT13', 'Activity (Horseback Riding)'),
    ('ACT14', 'Activity (Ice Skating)'),
    ('ACT15', 'Activity (Karaoke)'),
    ('ACT16', 'Activity (Mini Golf)'),
    ('ACT17', 'Activity (Movies)'),
    ('ACT18', 'Activity (Musuem)'),
    ('ACT19', 'Activity (Painting)'),
    ('ACT20', 'Activity (Park)'),
    ('ACT21', 'Activity (Play)'),
    ('ACT22', 'Activity (Zoo)'),

    ('AMU', 'Amusement Park'),
    ('DES', 'Dessert (D)'),
    ('DES_P', 'Dessert (D/P)'),
    ('DIN', 'Dinner (D)'),
    ('DIN_D', 'Dinner (Deal)'),
    ('DIN_M', 'Dinner (M)'),
    ('LUN', 'Lunch (D)'),
    ('STA', 'Stadium'),
    ('WEB', 'Website'),
    )

class AddDateForm(forms.ModelForm):
# how do you make some of them optional input?
    parking = forms.CharField(required=False)
    maps = forms.URLField(required=False)

    category = forms.ChoiceField(choices=CATEGORIES, required=True )

    class Meta:
        model = Dates

        fields = [
            "place", 
            "category", 
            "address", 
            "area", 
            "state", 
            "phone", 
            "website",
            "notes", 
            "price", 
            "parking", 
            "maps", 
        ]

        widgets = {
            'place': forms.TextInput(attrs={'placeholder': 'Ex: Wolf and Lamb'}),
            'area': forms.TextInput(attrs={'placeholder': 'Ex: West Village'}),
            'state': forms.TextInput(attrs={'placeholder': 'Ex: NY'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Ex: 718-888-8080'}),
            'website': forms.TextInput(attrs={'placeholder': 'Ex: http://www.example.com'}),
            'notes': forms.TextInput(attrs={'placeholder': 'Ex: Was amazing'}),
            'price': forms.TextInput(attrs={'placeholder': 'Ex: $$'}),
            'parking': forms.TextInput(attrs={'placeholder': 'Ex: Street'}),
        }


# need a search form to get date ideas by catergory using check boxes
class SearchDateForm(forms.ModelForm):   
    category_choice = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple, choices=CATEGORIES)

    class Meta:
        model = Dates

        fields = [
            "category_choice", 
        ]





