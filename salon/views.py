# salon/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, Booking
from .forms import BookingForm

def home(request):
    services = Service.objects.all()
    return render(request, 'salon/home.html', {'services': services})

def about(request):
    return render(request, 'salon/about.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'salon/services.html', {'services': services})

def contact(request):
    return render(request, 'salon/contact.html')

def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your appointment has been booked successfully!')
            return redirect('book')  # Redirect to the booking page to display the message
        else:
            messages.error(request, 'There was an error with your booking. Please check the details and try again.')
    else:
        form = BookingForm()
# salon/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, Booking
from .forms import BookingForm

def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your appointment has been booked successfully!')
            return redirect('book')
        else:
            messages.error(request, 'There was an error with your booking. Please check the details and try again.')
    else:
        form = BookingForm()

    return render(request, 'salon/book.html', {'form': form})

    return render(request, 'salon/book.html', {'form': form})
