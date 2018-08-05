from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "this is the index page of app"

@app.route("/hello")
def Hello():
    return "you come to hello page now"