# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *

# Create your views here.
def index (request):
    context = {
        'courses': Course.objects.all()
    }

    return render (request, 'courses/index.html', context)

def addCourse (request):
    errors = Course.objects.basic_validator(request.POST)
    
    if errors:
        for error in errors:
            messages.error(request, error)
    else:
        Course.objects.create(name = request.POST['name'], desc = request.POST['desc'])
    #Course.objects.create (name=request.POST['name'], desc = request.POST['desc'])
    return redirect ('/')