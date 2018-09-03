from flask import Flask, url_for, render_template, request, g, make_response, after_this_request
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['file_path'] = '/home/lee/PycharmProjects/flask-study/files/'


@app.before_request
def set_user_lang():
    print('before request code running....')
    language = request.cookies.get('lan')

    if not language:
        language = 'cn'

        @after_this_request
        def remember_language(response):
            print('after request code running request code running....')
            response.set_cookie('lan', language)
            return response
    g.language = language


@app.route("/")
def index():
    username = request.cookies.get('name')
    lan = request.cookies.get('lan')
    return make_response(render_template('index.html', lan=lan))


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


@app.route('/fail-login')
def fail_login():
    fail_att = request.form['name']
    return ''


@app.route('/params')
def params():
    p_word = request.args.get('id')
    return p_word


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['my_file']
        f.save(app.config['file_path'] + secure_filename(f.filename))
    return render_template('upload.html')


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
