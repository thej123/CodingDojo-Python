from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import MySQLConnector
import re
import md5

emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app, 'the_wall_db')
app.secret_key = 'thewall'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/thewall')
def thewall():
    # print 'hello'

    query = "SELECT first_name FROM users WHERE id= :id"
    context = {
        'id': session['id']
        }
    firstname = mysql.query_db(query, context)

    query = "SELECT CONCAT(first_name, ' ', last_name, '-->', message) AS display_post_header, messages.id AS messageIDS FROM users LEFT JOIN messages ON messages.user_id = users.id"
    display_post = mysql.query_db(query, context)
    # print display_post

    return render_template('thewall.html',firstname=firstname[0]['first_name'], display_this=display_post)

@app.route('/logoff')
def logoff():
    return redirect("/")

@app.route('/user/register', methods=['POST'])
def register():

    count = 0

    query = 'SELECT email FROM users WHERE email = :newemail'
    content ={
        'newemail' : request.form['email']
    }
    if mysql.query_db(query, content):
        flash('This email has already been registered')
        count = 1
    if len(request.form['first_name']) < 2 or not (request.form['first_name']).isalpha():
        flash ('First_name should be atleast 2 characters and only letters')
        count = 1
    if len(request.form['last_name']) < 2 or not (request.form['last_name']).isalpha():
        flash ('Last_name should be atleast 2 characters and have only letters')
        count = 1
    if not emailRegex.match(request.form['email']):
        flash ('Email is not valid')
        count = 1
    if len(request.form['password']) <   9 or request.form['password']!=request.form['confirm_password']:
        flash ('Password should be atleast 8 characters long and should match the "Confirm Password"')
        count = 1
    if count == 0:
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())'
        content = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password' : md5.new(request.form['password']).hexdigest(),
        }
        mysql.query_db(query, content)
        flash('You have successfully registered!')
        query = "SELECT id FROM users WHERE email= :email"
        context = {
        'email': request.form['email']
        }
        id = mysql.query_db(query, context)
        # print id[0]['id']
        session['id'] = id[0]['id']
        # print session['id']
        return redirect('/thewall')
    else:
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
    
    password = mysql.query_db(query, context)

    if password[0]['password'] == md5.new(request.form['password']).hexdigest():
        flash('You have successfully logged in!')
        query = "SELECT id FROM users WHERE email= :email"
        context = {
        'email': request.form['email']
        }
        id = mysql.query_db(query, context)
        # print id[0]['id']
        session['id'] = id[0]['id']
        # print session['id']
        return redirect('/thewall')
    else:
        flash ('Login Credentials are Incorrect')
        return redirect('/')


@app.route('/message', methods=['POST'])
def message():
    if len(request.form['message']) > 0:
        query = 'INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:id, :message, NOW(), NOW())'
        content = {
            'message' : request.form['message'],
            'id' : session['id']
        }
        mysql.query_db(query, content)

    return redirect('/thewall')

@app.route('/comment', methods=['POST'])

def comment():
    print 'hello'
    if len(request.form['comment']) > 0:
        query = 'INSERT INTO comments (comment, created_at, updated_at, message_id, user_id) VALUES (:comment, NOW(), NOW(), :message_id, :user_id)'
        content = {
            'comment' : request.form['comment'],
            'message_id' : request.form['hidden_message_id'],
            'user_id' : session['id']
        }
        mysql.query_db(query, content)

    return redirect('/thewall')


app.run(debug=True)