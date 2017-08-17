from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
# Create your views here.

def index(request):
    context = {
        'data' : Course.objects.all()
    }
    return render(request, 'coursesApp/index.html', context)

def check(request, id):
    context = {
        'data' : Course.objects.get(id=id)
    }
    return render(request, 'coursesApp/destroy.html', context)

def add(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request,error, extra_tags=tag)
            return redirect('/coursesApp')
    else:
        Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
    return redirect('/coursesApp')

def destroy(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/coursesApp')



