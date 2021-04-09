import flask

app = flask.Flask(__name__)


# @app.route('/')
# def hello_world():
#    return 'Hello World'
@app.route('/')
def index():
    return flask.redirect(flask.url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['password']
        # some code contact with database
        
    return flask.render_template("login.html")


@app.route('/signup',methods=['GET', 'POST'])
def signup():
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['password']
        # print(username)
        # print(password)

        # some code contact with database

    return flask.render_template("signup.html")


if __name__ == '__main__':
    app.run()
