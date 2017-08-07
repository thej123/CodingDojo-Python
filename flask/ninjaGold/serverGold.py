from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = 'Ninja Gold'

@app.route('/')
def index():
    session['total'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def calc():
    # clickpath = request.form['name']
    # print request.form['Farm']
    # print request.form['Cave']
    # print request.form['Casino']
    building = request.form['building']
    print building

    if building == 'farm':
        farmvar = random.randrange(10,21)
        # print farmvar
    elif building == 'cave':
        farmvar = random.randrange(5,11)
        # print farmvar
    elif building == 'house':
        farmvar = random.randrange(2,6)
        # print farmvar
    elif building == 'reset':
        return redirect('/') 
        # session['total'] = 0

        # print farmvar
    else: 
        # request.form['Casino'] == 'four':
        farmvar = random.randrange(-50,51)
        # print farmvar
    print farmvar

    # if 'total' in session.keys():
    session['total'] += farmvar
    # else:
    #     session['total'] = 0
    print session['total']

    return render_template('index.html', total=session['total'], gold=farmvar, building=building)


app.run(debug=True)