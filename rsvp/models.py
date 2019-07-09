from django.db import models

# Create your models here.
class Guest(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=254, default='test@example.com')
    ATTENDING = 'Y'
    NOT_ATTENDING = 'N'
    RSVP_CHOICES = [
        (ATTENDING, 'ATTENDING'),
        (NOT_ATTENDING, 'NOT ABLE TO ATTEND'),
    ]
    rsvp = models.CharField(max_length=1, choices=RSVP_CHOICES, default=ATTENDING,)

    def __str__(self):
        return self.name
