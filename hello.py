from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "this is the index page of app"


@app.route("/hello")
def hello():
    return "you come to hello page now"


@app.route("/user/<userid>")
def show_user(userid):
    return 'this is userid: %s' % userid
