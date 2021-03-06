# Generated by Django 2.0.13 on 2019-07-07 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0002_attending'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attending',
            name='guest',
        ),
        migrations.AddField(
            model_name='guest',
            name='email_address',
            field=models.EmailField(default='test@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='guest',
            name='rsvp',
            field=models.CharField(choices=[('Y', 'ATTENDING'), ('N', 'NOT ABLE TO ATTEND')], default='Y', max_length=1),
        ),
        migrations.DeleteModel(
            name='Attending',
        ),
    ]
