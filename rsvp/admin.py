from django.contrib import admin

from .models import Guest

# Register your models here.
@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email_address', 'rsvp')
