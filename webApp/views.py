from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils.text import capfirst
from .models import *

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

def team(request):
    return render(request,'team.html')

def testimonials(request):
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
