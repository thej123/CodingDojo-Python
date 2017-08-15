from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    print 'hello'
    try:
        request.session['counter'] +=1
        print 'again'
    except:
        request.session['counter'] = 0
    unique_id = get_random_string(length=14)
    randword = {
        'word' : unique_id
    }
    return render(request, 'wordGEn/index.html', randword)

def process(request):
    return redirect('/wordGEn')

def reset(request):
    request.session['counter'] = 0
    return redirect('/wordGEn')