from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    # request.session.clear()
    if 'number_of_items' not in request.session:
        request.session['number_of_items'] = 0
    if 'total_cost' not in request.session:
        request.session['total_cost'] = 0
    return render(request, 'amadon/index.html')

def process(request):
    prices = { '1':19.99, '2':29.99, '3':4.99,'4':49.99}
    x = prices[request.POST['item']]
    y = float(request.POST['quantity'])
    request.session['total'] = x * y

    request.session['number_of_items'] += int(y)
    request.session['total_cost'] += request.session['total']
    
    return redirect('/checkout')



def checkout(request):
    return render(request, 'amadon/checkout.html')


def reset(request):
    request.session.clear()
    return redirect('/')