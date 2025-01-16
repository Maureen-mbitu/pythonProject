from django.shortcuts import render, redirect
from .models import Service, BlogPost, Appointment
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import ContactForm, AppointmentForm

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})