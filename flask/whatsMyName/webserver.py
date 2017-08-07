from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods = ["POST"])
def process():
    print "Got Post Info"
    session['name'] = request.form["name"]
    session['email'] = request.form["email"]
    return redirect("/show")

@app.route("/show")
def show_user():
    return render_template("success.html")

app.run(debug = True)