from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return "this is the index page of app"


@app.route('/login', methods=['GET', 'POST'])
def login():
    err = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            err = 'Invalid login info'
    return render_template('login.html', error=err)


def valid_login(name, pwd):
    if name == 'lee' and pwd == '123':
        return True
    else:
        return False


def log_the_user_in(name):
    print('user {} logged in'.format(name))
    return render_template('welcome.html', name=name)


@app.route("/hello/")
@app.route('/hello/<name>')
def hello(name=None):
    print('call hello')
    # g.fuck = 'test fucking g'
    return render_template('hello.j2', name=name)


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
    return 'hello go page,cant use /'


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='lee leon'))
#     print(url_for('hello', username='lee leon'))


with app.test_request_context('/hello', method='post'):
    assert request.path == '/hello'
    print(request.method)
    assert request.method == 'POST'


# with app.request_context(environ):
#     assert request.method == 'POST'
