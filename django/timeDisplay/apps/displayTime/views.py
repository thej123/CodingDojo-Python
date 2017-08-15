from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime
# Create your views here.

def index(request):
    context = {
    "time": strftime("%B %d%, %Y %H:%M %p", gmtime())
    }
    # print context
    return render(request, 'displayTime/index.html', context)