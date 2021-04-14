import flask
import database

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


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['password']
        # print(username)
        # print(password)

        # some code contact with database

    return flask.render_template("signup.html")


@app.route('/mainpage', methods=['GET'])
def main_page():
    # some code contact with database

    # some code reform the main page html based on the user id

    userid = "1"
    return flask.render_template("mainpage.html", userid=userid)


if __name__ == '__main__':
    app.run()
