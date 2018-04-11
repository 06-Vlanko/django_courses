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
        for tag,error in errors.iteritems():
            messages.error(request, error)
    else:
        Course.objects.create(name = request.POST['name'], desc = request.POST['desc'])
    return redirect ('/')

def destroy(request, course_id):

    ID = {
        'course_id': course_id,
        'course': Course.objects.get(id=course_id)
    }

    return render (request, 'courses/check.html', ID)

def yes_destroy(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect ('/')