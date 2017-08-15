from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    
    return render(request, 'surveyForm/index.html')

def process(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        # print request.session['name']
        # print request.session['location']
        # print request.session['language']
        # print request.session['comment']
    return redirect('/results')

def results(request):
    if (not request.session['counter']):
        request.session['counter'] = 1
    request.session['counter'] += 1
    return render(request, 'surveyForm/results.html')