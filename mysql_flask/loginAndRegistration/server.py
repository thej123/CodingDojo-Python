from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import MySQLConnector
import re
import md5

# nameRegex = re.compile(r'^[a-zA-Z]+$')
emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app, 'LoRegdb')
app.secret_key = 'itssecret'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user/register', methods=['POST'])
def register():
    # print request.form['first_name']
    if len(request.form['first_name']) < 2 or not (request.form['first_name']).isalpha():
        flash ('First_name should be atleast 2 characters and only letters')
    elif len(request.form['last_name']) < 2 or not (request.form['last_name']).isalpha():
        flash ('Last_name should be atleast 2 characters and have only letters')
    elif not emailRegex.match(request.form['email']):
        flash ('Email is not valid')
    elif len(request.form['password']) <   9 or request.form['password']!=request.form['confirm_password']:
        flash ('Password should be atleast 8 characters long and should match the "Confirm Password"')
    else:
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())'
        content = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password' : md5.new(request.form['password']).hexdigest(),
        }
        mysql.query_db(query, content)
        flash('You have successfully registered!')
        return render_template('/loggedin.html')
    return redirect('/')

@app.route('/user/login', methods=['POST'])
def login():

    query = 'SELECT password FROM users WHERE email= :email'
    context = {
        'email': request.form['email']
    }
    if not (mysql.query_db(query, context)):
        flash ('Login Credentials are Incorrect')
        return redirect('/')
    
    data = mysql.query_db(query, context)

    if data[0]['password'] == md5.new(request.form['password']).hexdigest():
        flash('You have successfully logged in!')
        return render_template('loggedin.html')
    else:
        flash ('Login Credentials are Incorrect')
        return redirect('/')

@app.route('/goback')
def goback():
    return redirect("/")

app.run(debug=True)