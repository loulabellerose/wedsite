from django import forms
from .models import Guest
from django.utils.translation import gettext_lazy as _

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('name', 'phone_number', 'rsvp', 'email_address')
        labels = {
            'rsvp': _('RSVP'),
        }
        widgets = {
            'rsvp': forms.Select(attrs={'class': 'dropdown'}),
        }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    contact_email = forms.CharField(max_length=100)
    message = forms.CharField(max_length=1000)
