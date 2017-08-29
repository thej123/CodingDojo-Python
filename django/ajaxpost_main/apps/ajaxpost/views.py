from django.shortcuts import render, HttpResponse, redirect
from models import *
# Create your views here.

def index(request):
    return render(request, 'ajaxpost/index.html')

def create(request):
    # print 'went to "create" method'
    Post.objects.create(post=request.POST['notes'])
    posts = Post.objects.get(post=request.POST['notes'])
    return render(request, 'ajaxpost/note.html', {'posts':posts})