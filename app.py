from flask import Flask, url_for, template_rendered

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return "this is the index page of app"


@app.route('/login')
def login():
    return 'login'


@app.route("/hello/")
@app.route('/hello/<name>')
def hello(name=None):
    print('call hello')
    # g.fuck = 'test fucking g'
    return template_rendered('hello.html', name=name)


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
    # test git pass
    # remember?
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


