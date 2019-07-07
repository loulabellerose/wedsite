from django import forms
from .models import Guest

class GuestForm(forms.ModelForm):

    class Meta:
        model = Guest
        fields = ('name', 'phone_number', 'email_address', 'rsvp')
