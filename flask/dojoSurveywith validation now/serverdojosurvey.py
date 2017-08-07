from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods = ["POST"])
def result():
    # print "Got Post Info"
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]
    if len(request.form['name']) < 1:
        flash('Name cannot be empty!')
    else:
        flash('Success! Your name is: {}'.format(request.form['name']))
    
    if len(request.form['comment']) < 1:
        flash('Comment cannot be empty!')
    elif len(request.form['comment']) > 120:
        flash('Comment cannot be bigger than 120 characters!')
    else:
        flash('Success! Your comment is: {}'.format(request.form['name']))


    
    return render_template("result.html", name=name, location=location, language=language, comment=comment)

@app.route("/goback")
def goback():
    return redirect("/")


app.run(debug = True)