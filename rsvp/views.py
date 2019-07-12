from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Guest
from .forms import GuestForm, ContactForm
from django.core.mail import send_mail

def index(request):
        if request.method == "POST":
            form = GuestForm(request.POST)

            if form.is_valid():
                guest = form.save()
                guest.save()
                return redirect('thanks')
        else:
            form = GuestForm()
        return render(request, 'rsvp/index.html', {'form': form})

def respond(request):
    if request.method == "POST":
        form = GuestForm(request.POST)

        if form.is_valid():
            guest = form.save()
            guest.save()
            return redirect('thanks')
    else:
        form = GuestForm()
    return render(request, 'rsvp/index.html', {'form': form})

def thanks(request):
    return render(request, 'rsvp/thanks.html')

def contact(request):
    form = ContactForm()
    if form.is_valid():
        return redirect('message-sent')
    else:
        form = ContactForm()
    return render(request, 'rsvp/contact-us.html')

def message_sent(request):
    return render(request, 'rsvp/message-sent.html')
