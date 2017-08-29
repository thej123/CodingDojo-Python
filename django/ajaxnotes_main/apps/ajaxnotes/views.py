from django.shortcuts import render, redirect
from models import *

# Create your views here.

def index(request):
    notes = Note.objects.all()
    return render(request, 'ajaxnotes/index.html', {'notes':notes})

def create(request):
    print'hello'
    Note.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    note = Note.objects.last()
    print note
    return render(request, 'ajaxnotes/display.html', {'note':note})

def delete(request, note_id):
    print'hello'
    Note.objects.get(id=note_id).delete()
    return redirect('/')