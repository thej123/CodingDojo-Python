from django.shortcuts import render, redirect
import random
# Create your views here.

def index(request):
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'lines' not in request.session:
        request.session['lines'] = []
    return render(request, 'ninja_gold/index.html')

def process(request):
    building = request.POST['building']

    if building == 'farm':
        farmvar = random.randrange(10,21)
    elif building == 'cave':
        farmvar = random.randrange(5,11)
    elif building == 'house':
        farmvar = random.randrange(2,6)
    elif building == 'reset':
        request.session.clear()
        return redirect('/') 
    else: 
        farmvar = random.randrange(-50,51)

    try:
        content
    except:
        content = []
    temp = content
    temp.append('Earned {} golds from the {}'.format(farmvar, building))
    content = temp
    
    request.session['lines'] += content
    print content

    request.session['total'] += farmvar
    return redirect('/')
