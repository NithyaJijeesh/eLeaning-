from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils.text import capfirst
from .models import *

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def courses(request):
    return render(request,'courses.html')

def contact(request):
    return render(request,'contact.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')

def placement(request):
    return render(request,'placement.html')

def vision(request):
    return render(request,'vision.html')

def blogs(request):
    return render(request,'blog.html')

def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        Subscriber(email = email).save()
    return redirect('/')
