from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Guest
from .forms import GuestForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

def respond(request):
    if request.method == "POST":
        form = GuestForm(request.POST)

        if form.is_valid():
            guest = form.save()
            guest.save()
            return redirect('thanks')
    else:
        form = GuestForm()
    return render(request, 'rsvp/respond.html', {'form': form})

def thanks(request):
    return HttpResponse("Thanks for RSVP-ing!")
