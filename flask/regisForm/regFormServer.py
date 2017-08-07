from flask import Flask, render_template, redirect, flash, request
import re

emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# passwordCapRegex = re.compile(r'^(?=.*[A-Z])+$')
# passwordNumRegex = re.compile(r'^(?=.*\d)+$')
app = Flask(__name__)
app.secret_key = 'tiredBro'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['email']) < 1:
        flash('Email cannot be empty!')
    elif not emailRegex.match(request.form['email']):
        flash('Invalid Email Address!')
    else:
        flash('Success! Your Email is: {}'.format(request.form['email']))
    
    if len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1:
        flash('Names cannot be empty!')
    elif not (request.form['first_name']).isalpha() or not (request.form['last_name']).isalpha():
        flash('Names cannot contain any numbers!')
        print request.form['first_name'].isalpha()
    else:
        flash('Success! Your First Name is: {}'.format(request.form['first_name']))
        flash('Success! Your Last Name is: {}'.format(request.form['last_name']))
    
    if len(request.form['password']) < 1 or len(request.form['confirm_password']) < 1:
        flash('Passwords cannot be empty!')
    elif len(request.form['password']) > 9 or len(request.form['confirm_password']) > 9:
        flash('Passwords cannot be more than 8 characters!')
    # elif not passwordCapRegex(request.form['password']) or not passwordCapRegex(request.form['confirm_password']):
    #     flash('Passwords need atleast one Capital letter!')
    elif (request.form['password']) != (request.form['confirm_password']):
        flash('Passwords are not matching!')
    
    else:
        flash('Success!')

    # return render_template("result.html")
    return redirect("/show")

@app.route('/show')
def show_results():
    return render_template("results.html")
    
@app.route("/goback")
def goback():
    return redirect("/")

app.run(debug=True)