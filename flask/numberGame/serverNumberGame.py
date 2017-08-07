from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key = "ThisGame"

@app.route('/')
def index():
    session['someKey'] = random.randrange(0,101)
    print session['someKey']
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def calc():
    print "Got Submission"
    session['number'] = request.form["number"]
    print session['number']
    print session['someKey']
    a = int(session['number'])
    b = int(session['someKey'])
    play = 'none'
    # c = False
    # if c = False:
    if a > b:
        print "too high"
        comment = "too high"
    elif a < b:
        print "too low"
        comment = "too low"
    else:
        print session['number'] + "was the number!"
        comment = session['number'] + " was the number! YOU GOT IT"
        # c = True
        play = 'play'
        
    return render_template('index.html', comment=comment, play=play)
#     else:

#         return render_template('index.html', comment=comment)
# @app.route('/process')
# def run():
#     return render_template('index.html')

app.run(debug=True)