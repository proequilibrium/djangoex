from django import forms
from .models import Event, EventRun

class addEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields=[
            'host',
            'name',
            'description',
            'location',
            'category',
        ]


class AddEventRunForm(forms.ModelForm):
    class Meta:
        model=EventRun
        fields=[
            'event',
            'happens',
            'seats_available',
            'price',
        ]
