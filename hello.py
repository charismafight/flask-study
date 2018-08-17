from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "this is the index page of app"


@app.route("/hello/")
def hello():
    print('call hello')
    return "you come to hello page now"


@app.route("/user/<userid>")
def show_user(userid):
    return 'this is userid: %s' % userid


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return subpath


@app.route('/<table>/<tttt>')
def show_data(table, tttt):
    return table+tttt


@app.route('/hello-go')
def hello_go():
    #test git pass
    #remember?
    return 'hello go page,cant use /'
