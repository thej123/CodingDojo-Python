from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route("/")
def index():

    if 'count' in session.keys():
        session['count'] += 1
    else:
        session['count'] = 1

    # try:
    #     session['count'] += 1
    # except KeyError:
    #     session['count'] = 1
    return render_template('index.html')

# @app.route('/process', methods=['POST'])
# def keepcount():
#     session['count'] += 1
#     return redirect('/')

@app.route('/processTwo', methods=['POST'])
def keepcountByTwo():
    session['count'] += 1
    return redirect('/')

@app.route('/processReset', methods=['POST'])
def resetcount():
    session['count'] = 0
    return redirect('/')

app.run(debug = True)