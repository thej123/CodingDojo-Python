from flask import Flask, render_template          # Import Flask to allow us to create our app.
app = Flask(__name__)                            # Global variable __name__ tells Flask whether or not we are running the file
                                                  # directly, or importing it as a module.
@app.route('/')
def hello_world():
  return render_template("index.html")                           # Return the string 'Hello World!' as a response.

@app.route('/projects')
def projects():
  return render_template("projects.html")

@app.route('/about')
def about():
  return render_template("about.html")
 







app.run(debug=True)                                # Run the app in debug mode.from flask import Flask
