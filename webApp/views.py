from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils.text import capfirst

def index(request):

    return render(request,'index.html')