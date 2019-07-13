from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Guest
from .forms import GuestForm, ContactForm
from django.core.mail import send_mail, BadHeaderError

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

def thanks(request):
    return render(request, 'rsvp/thanks.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            contact_email = form.cleaned_data['contact_email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, contact_email, ['louiserosehamerston@gmail.com'], fail_silenty=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            messages.success(request, 'Form submission successful')
            return redirect('message-sent')
    else:
        form = ContactForm()
    return render(request, "rsvp/contact-us.html", {'form': form})

def message_sent(request):
    return render(request, 'rsvp/message-sent.html')
