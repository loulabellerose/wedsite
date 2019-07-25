from django import forms
from .models import Guest
from django.utils.translation import gettext_lazy as _

class GuestForm(forms.ModelForm):
    email_address = forms.EmailField(max_length=200, required=False, help_text='If you dont have one leave blank')

    class Meta:
        model = Guest
        fields = ('name', 'phone_number', 'rsvp')
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
