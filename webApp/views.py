from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils.text import capfirst
from .models import *
import random



def index(request):
    video = about_model.objects.all()
    courses = course_details.objects.all()
    mentors = instructors.objects.all()
    reviews = testimonial.objects.all()
    context = {
        'video' : video,
        'courses' :courses,
        'mentors' : mentors,
        'review' :reviews
    }
    return render(request,'index.html',context)

def about(request):
    video = about_model.objects.all()
    mentors = instructors.objects.all()

    context = {
        'video' : video,
        'mentors' : mentors,
    }
    return render(request,'about.html', context)

def courses(request):
    courses = course_details.objects.all()
    context = {
        'courses' : courses,
    }
    return render(request,'courses.html',context)

def contact(request):
    return render(request,'contact.html')


def placement(request):
    return render(request,'placement.html')


def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        Subscriber(email = email).save()
    return redirect('/')
def contactuss(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['msg']
    
        contactus(name = name, email = email, subject = subject, message = message).save()

    return redirect('/contact')
