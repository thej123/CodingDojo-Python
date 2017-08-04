from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/red")
# def red():
#     return render_template("red.html")

# @app.route("/blue")
# def blue():
#     return render_template("blue.html")

# @app.route("/orange")
# def orange():
#     return render_template("orange.html")

# @app.route("/purple")
# def purple():
#     return render_template("purple.html")

@app.route("/<color>")
def findcolor(color):
#     newcolor = color
#     print newcolor
#     if newcolor == "red":
#         return render_template("red.html")
#     elif newcolor == "blue":
#         return render_template("blue.html")
#     elif newcolor == "orange":
#         return render_template("orange.html")
#     elif newcolor == "purple":
#         return render_template("purple.html")
#     else:
#         return render_template("girl.html")

    if color == "ninja":
        color = url_for('static', filename='images/tm mnt.png')
    elif color == "red":
        color = url_for('static', filename='images/raphael.jpg')
    elif color == "blue":
        color = url_for('static', filename='images/leonardo.jpg')
    elif color == "orange":
        color = url_for('static', filename='images/michelangelo.jpg')
    elif color == "purple":
        color = url_for('static', filename='images/donatello.jpg')
    else:
        color = url_for('static', filename='images/notapril.jpg')

    return render_template("purple.html", color = color)



app.run(debug = True)