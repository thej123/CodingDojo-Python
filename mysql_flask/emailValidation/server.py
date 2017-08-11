from flask import Flask, render_template, redirect, flash, request, session
from mysqlconnection import MySQLConnector
import re

emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app, 'email_validationdb')
app.secret_key = 'emailValid'

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/process', methods=['POST'])
def check_email():
    if len(request.form['email']) < 1:
        flash('Email cannot be empty!')
        return redirect('/')
    elif not emailRegex.match(request.form['email']):
        flash('Email is not valid!')
        return redirect('/')
    else:
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
            'email': request.form['email'],
        }   
        mysql.query_db(query, data)
        flash('The email address you entered ' + request.form['email'] + " is a VALID email address! Thank you!")
        return redirect('/success')

@app.route('/success')
def display():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template('success.html', all_emails = emails)

@app.route('/goback')
def goback():
    return redirect('/')

app.run(debug=True)