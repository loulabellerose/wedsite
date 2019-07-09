from django import forms
from .models import Guest
from django.utils.translation import gettext_lazy as _

class GuestForm(forms.ModelForm):

    class Meta:
        model = Guest
        fields = ('name', 'phone_number', 'email_address', 'rsvp')
        labels = {
            'rsvp': _('RSVP'),
        }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
