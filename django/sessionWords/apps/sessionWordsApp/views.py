from __future__ import unicode_literals
from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'sessionWordsApp/index.html')

def add(request):
    if (request.POST['word']):
        wordList = {}
        for key, value in request.POST.iteritems():
            wordList[key] = value
            if key == 'bold':
                wordList['big'] = 'big'
            else:
                wordList['big'] = ''
        wordList['created_at'] = datetime.now().strftime('%H:%M %p, %B %d, %Y')
        try:
            request.session['words']
        except KeyError:
            request.session['words'] = []

        tempList = request.session['words']
        tempList.append(wordList)
        request.session['words'] = tempList

        # for key, val in request.session.__dict__.iteritems():
        #     print key, val
        # print 'past created at', 



    # if request.method == 'POST':
    #     if (not request.POST['word']):
    #         return redirect('/sessionWordsApp')
    #     else:
    #         if 'word' in request.session:
    #             request.session['word'] += [request.POST['word']]
    #         else:
    #             request.session['word'] = [request.POST['word']]
            
    #         print request.POST['color']
        # if request.POST['red'] == 'on':
        #     print 'hello'
        # request.session['bold'] = request.POST['bold']

    return redirect('/sessionWordsApp')

def clear(request):
    for x in request.session.keys():
        del request.session[x]
    return redirect('/sessionWordsApp')